import openai
import streamlit as st
import os

st.title("💬 Simple Chatbot")
st.caption("🚀 Validando chat v0.0.1")

#openai_api_key = st.session_state.get("OPENAI_API_KEY") or os.environ.get('OPENAI_API_KEY')
open_ai_key = st.secrets['open_ai'].open_ai_key #--> This in the deployed repo has to be enabled along with the openai_api_key=open_ai_key

if "simple_chat_messages" not in st.session_state:
    st.session_state["simple_chat_messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.simple_chat_messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
# EQUIVALENT TO
# prompt = st.chat_input()
# if prompt: 
if prompt := st.chat_input():
    if not open_ai_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = open_ai_key

    st.session_state.simple_chat_messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=st.session_state.simple_chat_messages)

    print("PRINTING REPSONSE")
    print(response)

    msg = response.choices[0].message
    st.session_state.simple_chat_messages.append(msg)
    st.chat_message("assistant").write(msg.content)
