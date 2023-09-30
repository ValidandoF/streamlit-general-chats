import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os

st.title("🦜🔗 Langchain - Idea Enhancement Outline Generator App")

#openai_api_key = st.session_state.get("OPENAI_API_KEY") or os.environ.get('OPENAI_API_KEY')
open_ai_key = st.secrets['open_ai'].open_ai_key #--> This in the deployed repo has to be enabled along with the openai_api_key=open_ai_key


def idea_enhacer(idea):
    # Instantiate LLM model
    llm = OpenAI(model_name="gpt-3.5-turbo-16k", openai_api_key=open_ai_key)

    # Prompt
    #template = "As a brilliant and excellent entrepenur and startups counselor or advisor, generate an outline for a idea about {idea}."
    template = "As a brilliant and excellent entrepenur and startups counselor or advisor, first improve idea provided and then outline key market features (max 5) to consider. Idea: {idea}"
    prompt = PromptTemplate(input_variables=["idea"], template=template)
    prompt_query = prompt.format(idea=idea)
    
    # Run LLM model
    response = llm(prompt_query)

    # Print results
    return st.info(response)


with st.form("myform"):
    topic_text = st.text_input("Enter prompt:", "")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        idea_enhacer(topic_text)