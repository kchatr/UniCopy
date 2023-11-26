import gradio as gr
import cohere

def chat(message):
    co = cohere.Client('Gx29SVN2CnTY3yZtqJQEYwgfQpSlN6m11yMU1mpF')

    response = co.chat(
	message, 
	model="command-nightly", 
	temperature=0.9)

    answer = response.text

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