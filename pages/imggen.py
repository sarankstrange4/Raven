import streamlit as st
from openai import OpenAI

st.title("DALL-E-3 Image Generation")

# Initialize OpenAI client
client = OpenAI(api_key='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')

# Function to generate image based on prompt
def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    if response and response.data:
        return response.data[0].url
    else:
        return None

# Streamlit UI
prompt = st.text_input("Enter prompt:")
if st.button("Generate Image"):
    if prompt:
        st.write("Generating image...")
        image_url = generate_image(prompt)
        if image_url:
            st.image(image_url, caption="Generated Image", use_column_width=True)
        else:
            st.write("Failed to generate image. Please try again.")
    else:
        st.write("Please enter a prompt.")
