
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


#Prompt template

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class coder and technical bug solver."),
    ("user", "{input}")
])

st.title("langchain demo")
input_text = st.text_input("enter your query")

llm = Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'input':input_text}))