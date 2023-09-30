import os
import streamlit as st

from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun


st.title("🔎 LangChain - Chat with search")

"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
"""

#openai_api_key = st.session_state.get("OPENAI_API_KEY") or os.environ.get('OPENAI_API_KEY')
open_ai_key = st.secrets['open_ai'].open_ai_key #--> This in the deployed repo has to be enabled along with the openai_api_key=open_ai_key


if "search_agent_messages" not in st.session_state:
    st.session_state["search_agent_messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

for msg in st.session_state.search_agent_messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Who won the Women's U.S. Open in 2018?"):
    st.session_state.search_agent_messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    if not open_ai_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=open_ai_key, streaming=True)
    search = DuckDuckGoSearchRun(name="Search")

    search_agent = initialize_agent(
        [search], 
        llm, 
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        handle_parsing_errors=True
    )

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.search_agent_messages, callbacks=[st_cb])
        st.session_state.search_agent_messages.append({"role": "assistant", "content": response})
        st.write(response)