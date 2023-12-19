from my_html_parser import qna_data
import yaml
import os

training_data = {"nlu": []}
responses_data = {}
stories_data = {"stories": []}
count = 0


suggestions_list = []
for heading, examples in qna_data.items():

# nlu_data = {
#     "nlu": [
#         {"intent": "greet", "examples": ["hey", "hello", "hi"]}
#     ]
# }
    # Add intent data to training_data
    intent = "intent_" + str(count)
    training_data["nlu"].append({"intent": intent, "examples": [str(heading)]})
    print(heading)
    suggestions_list.append(heading)

# responses = {
#     "utter_greet": [
#         {"text": "Hey there!"}
#     ]
# }


    utter = "utter_" + str(count)
    examples = "".join(examples)
    
    responses_data[utter] = [{"text": examples}]

# stories = {
#     "stories": [
#         {
#             "story": "happy path", 
#             "steps": [
#                 {"intent": "greet", "action": "utter_greet"} 
#             ]
#         }
#     ]
# }
    
    story_name = f"story_{count}"
    story = {"story": story_name, "steps": [{"intent": intent,"action": utter}]}
    stories_data["stories"].append(story)
    count += 1

print(suggestions_list)



#    nlu.yml file updates
nlu_file_path = "data/nlu.yml"
with open(nlu_file_path, "a") as file:
    file.write("\n")
    for item in training_data["nlu"]:
        intent_name = item["intent"]
        examples = item["examples"]
        
        # Write the intent name and examples to nlu.yml
        file.write(f"- intent: {intent_name}\n")
        file.write(f"  examples: |\n")
        
        # Write each example with proper indentation
        if isinstance(examples, list):
            for example in examples:
                file.write(f"    - {example}\n")
                file.write("\n")
        else:
            # If examples is a string, split it by newline and write each line
            for line in examples.split("\n"):
                file.write(f"    - {line}\n")









#   stories.yml file updates
stories_file_path = "data/stories.yml"
with open(stories_file_path, "a") as file:
    for story in stories_data["stories"]:
        story_name = story["story"]
        steps = story["steps"]
        
        file.write("\n")
        file.write(f"- story: {story_name}\n")
        file.write("  steps:\n")
        
        for step in steps:
            intent = step.get("intent")
            action = step.get("action")
            
            if intent:
                file.write(f"    - intent: {intent}\n")
            if action:
                file.write(f"    - action: {action}\n")
        
        file.write("\n")












# domain file 
# Load existing domain data
with open("domain.yml", "r") as file:
    domain_data = yaml.safe_load(file)

# Add new intents
intents_from_nlu = [item["intent"] for item in training_data["nlu"]]
domain_data["intents"].extend(intents_from_nlu)

# Add new responses




domain_data["responses"].update(responses_data)

# Write the updated domain data back to the file
with open("domain.yml", "w") as file:
    yaml.dump(domain_data, file, default_flow_style=False)