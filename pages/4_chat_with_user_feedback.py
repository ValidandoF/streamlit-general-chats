import openai
import streamlit as st
from trubrics.integrations.streamlit import FeedbackCollector
import os

st.title("📝 Chat with feedback enabled")

#openai_api_key = st.session_state.get("OPENAI_API_KEY") or os.environ.get('OPENAI_API_KEY')
open_ai_key = st.secrets['open_ai'].open_ai_key #--> This in the deployed repo has to be enabled along with the openai_api_key=open_ai_key


if "user_feedback_messages" not in st.session_state:
    st.session_state.user_feedback_messages = [
        {"role": "assistant", "content": "How can I help you? Leave feedback to help me improve!"}
    ]
if "response" not in st.session_state:
    st.session_state["response"] = None

user_feedback_messages = st.session_state.user_feedback_messages
for msg in user_feedback_messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Tell me a joke about sharks"):
    user_feedback_messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    if not open_ai_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    else:
        openai.api_key = open_ai_key
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=user_feedback_messages)
    st.session_state["response"] = response.choices[0].message.content

    with st.chat_message("assistant"):
        user_feedback_messages.append({"role": "assistant", "content": st.session_state["response"]})
        st.write(st.session_state["response"])

if st.session_state["response"]:
    if "TRUBRICS_EMAIL" in st.secrets["trubrics"]:
        collector = FeedbackCollector(
            project="validando-streamlit-app",
            email=st.secrets["trubrics"].TRUBRICS_EMAIL,
            password=st.secrets["trubrics"].TRUBRICS_PASSWORD,
        )

        collector.st_feedback(
            component="chat-test-2",
            model="gpt-3.5-turbo",
            open_feedback_label="[Optional] Please provide an explanation",
            prompt_id=None,  # see prompts to log prompts and model generations,
            feedback_type="thumbs",
            metadata={"chat": user_feedback_messages},
            key=f"feedbak_{len(user_feedback_messages)}",
            save_to_trubrics=True,
        )

        st.toast("Feedback recorded!", icon="📝")