from openai import OpenAI
import streamlit as st

# Sidebar setup
with st.sidebar:
    openai_api_key = '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'

# Main app
st.title("💬 RAVEN")
st.caption("🚀 AI ASSISTANT for MUSIC PROJECT BETA")

# Initialize session state if not present
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "you are an assistant like Jarvis, respond using 'sir'"}]

# Display existing messages
for msg in st.session_state.messages[1:]:  # Skip the first message
    st.chat_message(msg["role"]).write(msg["content"])

# Get user input and process it
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    # Initialize OpenAI client
    client = OpenAI(api_key=openai_api_key)

    # Add user input to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Generate response from OpenAI
    response = client.chat.completions.create(model="gpt-4-turbo", messages=st.session_state.messages[1:])  # Exclude the first message
    msg = response.choices[0].message.content

    # Add assistant response to session state and display it
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
