# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []




from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
import difflib

# class ActionBestMatchingSuggestions(Action):
#     def name(self) -> Text:
#         return "action_best_matching_suggestions"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Get user input
#         user_input = tracker.latest_message.get('text')

#         # Your suggestion list
#         suggestion_list = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

#         # Find best matching suggestions using difflib
#         best_matching_suggestions = difflib.get_close_matches(user_input, suggestion_list, n=4, cutoff=0.6)

#         # Construct a message with the selected suggestions
#         suggestions_message = "\n".join([f"- {suggestion}" for suggestion in best_matching_suggestions])

#         # Send the message to the user
#         dispatcher.utter_message("utter_out_of_scope", tracker)

#         return [UserUtteranceReverted()]




class ActionFallback(Action):
    def name(self) -> Text:
        return "action_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Provide a list of suggestions
        suggestions = ["Can you ask another question?", "I'm not sure. How about trying...", "Try asking in a different way."]
        dispatcher.utter_message(text="I'm sorry, I couldn't understand your question. Here are some suggestions:")
        dispatcher.utter_message(text="\n".join(suggestions))
        # dispatcher.utter_message(response="utter_didnt_get_that")
        # dispatcher.utter_message(response="utter_suggestions")
        # dispatcher.utter_message(response="utter_ask_rephrase")

        return [UserUtteranceReverted()]