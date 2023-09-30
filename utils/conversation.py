import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


def get_chat(name = "gpt-3.5-turbo-16k", temperature = 0) -> ChatOpenAI:
    chat = ChatOpenAI(model=name,
                      temperature=temperature,
                      max_tokens=-1,
                      max_retries=3,
                      streaming=True,
                      callbacks=[StreamingStdOutCallbackHandler()]     
                    )
    return chat

def clear_chat() -> None: 
    st.session_state.user_text = ""
    st.session_state.messages = []
    st.session_state.generated = []
    
    st.session_state.past = []

    st.session_state.costs = []
    st.session_state.total_tokens = []
    #st.session_state.seed = randrange(10**8)  # noqa: S311

def show_text_input() -> None:
    st.text_area(label=st.session_state.chat_placeholder, value=st.session_state.user_text, key="user_text")

# Define function to get user input
def get_text() -> str:
    """
    Get the user input text.

    Returns:
        (str): The text entered by the user
    """
    input_text = st.text_input("You: ", st.session_state["input"], 
                            key="input",
                            placeholder="Your AI assistant here! Ask me anything ...", 
                            label_visibility='hidden')
    return input_text

def get_chat_response() -> str:
    return 'HI'

