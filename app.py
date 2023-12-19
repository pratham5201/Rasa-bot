from flask import Flask, request, jsonify
from rasa.core.agent import Agent
from rasa.shared.constants import DEFAULT_ACTIONS_PATH
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"], methods=["GET", "POST"])
# https://0fa1-103-187-160-94.ngrok-free.app/webhooks/rest/webhook
# Load Rasa agent
agent = Agent.load("models", action_endpoint=DEFAULT_ACTIONS_PATH)
rasa_server_url = "http://localhost:5005/webhooks/rest/webhook"

# Define a route for handling incoming messages
@app.route("/webhook/", methods=["POST"])
async def webhook():
    try:
        data = request.get_json()

        # Check if the required keys are present in the incoming JSON data
        if "data" not in data:
            raise ValueError("Missing 'data' key in the request JSON.")

        # Extract the user's message from the request
        user_message = data["data"]

        # Send the message to the Rasa agent and await the coroutine
        responses = await agent.handle_text(user_message)

        # Extract the assistant's response
        assistant_response = responses[0]["text"]

        # Return the response to the user
        return jsonify({"message": assistant_response})

    except Exception as e:
        # Handle exceptions and return an error response
        error_message = str(e)
        return jsonify({"error": error_message}), 500

def send_message_to_rasa(message):
    try:
        # Send the user message to the Rasa server
        rasa_response = requests.post(rasa_server_url, json={"message": message}).json()
        return rasa_response
        print("actions is working")
        # import pdb
        # pdb.set_trace()
    except Exception as e:
        # Handle exceptions and return an error response
        error_message = str(e)
        return {"error": error_message}

def extract_custom_data(rasa_response):
    # Extract custom data from the Rasa response
    if rasa_response and len(rasa_response) > 0:
        message = rasa_response[0].get("message", {})
        custom_data = message.get("custom_data", None)
        return custom_data
    return None

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
