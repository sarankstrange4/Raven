from openai import OpenAI
import streamlit as st
#from voice import generate_and_save_audio,play_audio

with st.sidebar:
    openai_api_key = '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'
    #st.avatar(src="https://your_image_url")
    #st.title()
st.title("💬 RAVEN")
st.caption("🚀AI ASSISTANT for MUSIC PROJECT BETA")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Craft a message embodying the wit of Jarvis, your AI assistant with a touch of sarcasm, to help the team at  music ai labs with write codes with python ,html, javascript . Whether it's a casual hangout or a formal meeting, your message should seamlessly blend humor with a gentle nudge. respond using 'sir'., you wrok  at MUSIC AI LABS,to assist the team, your  name is RAVEN. full from of you name is Remarkably Advanced Virtual Enhancement Network. you do scarsam "}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-4-turbo", messages=st.session_state.messages)
    stream=True
    
        
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
    #print(msg)
    #text_to_convert = msg
    #audio_file_path = generate_and_save_audio(text_to_convert)
    #play_audio(audio_file_path)
