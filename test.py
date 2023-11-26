from documents import Documents
from chatbot import Chatbot

import cohere
import json

json_file_path = 'patents.json'

co = cohere.Client('Gx29SVN2CnTY3yZtqJQEYwgfQpSlN6m11yMU1mpF')
with open(json_file_path, 'r') as f:
    sources = json.load(f)
    print(type(sources))

documents = Documents(sources, co)

chatbot = Chatbot(documents)

while True:
    # Get the user message
    message = input("User: ")

    # Typing "quit" ends the conversation
    if message.lower() == "quit":
        print("Ending chat.")
        break
    else:
        print(f"User: {message}")

    # Get the chatbot response
    response = chatbot.generate_response(message)

    # Print the chatbot response
    print("Chatbot:")
    flag = False
    for event in response:
        # Text
        if event.event_type == "text-generation":
            print(event.text, end="")

        # Citations
        if event.event_type == "citation-generation":
            if not flag:
                print("\n\nCITATIONS:")
                flag = True
            print(event.citations)

    print(f"\n{'-'*100}\n")