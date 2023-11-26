import gradio as gr
import cohere

from flask_backend.documents import Documents
from chatbot import Chatbot
from flask_backend.preprocessing import get_sources

co = cohere.Client("Gx29SVN2CnTY3yZtqJQEYwgfQpSlN6m11yMU1mpF")

sources = get_sources()

documents = Documents(sources, co)

chatbot = Chatbot(documents, co)

def chat(message):
    response = co.chat(
	message, 
	model="command-nightly", 
	temperature=0.9)

    for event in response:
        if event.event_type == "text-generation":
            answer = event.text

    return answer


def ml_fcn(Patent):
    # Your ML logic here
    # Replace this with your actual ML function
    result = chat(Patent)
    # result = f"You entered: {Patent}"
    return result

demo = gr.Interface(fn=ml_fcn, inputs="text", outputs="text")
    
if __name__ == "__main__":
    demo.launch(show_api=False) 