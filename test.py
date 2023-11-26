from documents import Documents
from chatbot import Chatbot
from preprocessing import get_sources

import cohere
import json

co = cohere.Client("Gx29SVN2CnTY3yZtqJQEYwgfQpSlN6m11yMU1mpF")

sources = get_sources()

documents = Documents(sources, co)

chatbot = Chatbot(documents, co)

while True:
    # Get the user message
    message = input("User: ")

    # Typing "quit" ends the conversation
    if message.lower() == "quit":
        print("Ending chat.")
        break
    else:
        print(f"User: {message}")

    prompt = f"""
    {message}

    For any queries regarding the patent, please output the patent number corresponding to citations.
    """

    # Get the chatbot response
    response = chatbot.generate_response(prompt)

    # Print the chatbot response
    print("Chatbot:")
    flag = False
    print(response.text)

    print(f"\n{'-'*100}\n")