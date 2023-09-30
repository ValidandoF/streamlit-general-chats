#import openai
import streamlit as st

from components.sidebar import sidebar
from components.footer import footer

st.set_page_config(page_title="Validando Chat", page_icon="📖", layout="wide")
st.header("📖Validando Chat")

sidebar()

st.title("Validando chats lab")

st.subheader("Chat available")

chats_description = '''
1. Simple chat: Chat with just Open AI usage with gpt-3.5 model.

2. Search agent: Langchain agent with access to the internet through DuckDuckgo API and Langchain agent. By the way, pretty standard.

3. Langchain bot: Langchain bot starter with prompt customization with all answers being pesimist and angry. Just for fun.
'''

st.markdown(chats_description)

footer()

# if __name__ == "__main__":
#     run_agi()
