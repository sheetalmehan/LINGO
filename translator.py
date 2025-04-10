import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key=os.getenv("groq_api_key1")
# langsmith_api_key=os.getenv("LANGSMITH_API_KEY")
# tavily_api_key=os.getenv("tavily_api_key")

os.environ["groq_api_key1"]=groq_api_key
# os.environ["LANGSMITH_API_KEY"]=langsmith_api_key
# os.environ["TAVILY_API_KEY"]=tavily_api_key
from langchain_groq import ChatGroq

llm = ChatGroq(api_key=groq_api_key, model="llama3-70b-8192")
from langchain_community import output_parsers
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
st.set_page_config(page_title="LingoPilot - LangChain Translator", layout="centered")
st.title("🌍 LingoPilot")
st.subheader("Real-time translation powered by LLaMA 3 & Groq ⚡")

prompt_template=ChatPromptTemplate.from_messages([
    ("system","translate the following into this {language}"),
    ("human","{text}")
]) 
parser=StrOutputParser()
text = st.text_area("Enter text to translate:", height=150)
language = st.text_input("Enter target language (e.g., Spanish, French):")

# Translate button
if st.button("Translate"):
    if text and language:
        with st.spinner("Translating..."):
            messages = prompt_template.invoke({"language": language, "text": text})
            response = llm.invoke(messages)
            output = parser.invoke(response)
        st.success("✅ Translation Complete!")
        st.text_area("Translated Text:", output, height=150)
    else:
        st.warning("Please enter both the text and the target language.")