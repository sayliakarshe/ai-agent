import gradio as gr

# A simple function to classify text
def find_houses(t):
    return f"Hello, {name}!"

# Define the Gradio interface
iface = gr.Interface(fn=find_houses, inputs="text", outputs="text")

# Launch the demo
iface.launch(share=True)
