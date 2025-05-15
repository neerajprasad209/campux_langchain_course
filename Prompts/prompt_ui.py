from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = ChatOpenAI(model ="gpt-4o")



st.header("Reaserch Tools")
text = st.text_input("Enter your research question here:")

messages = [
    (
        "system",
        "You are a helpful ai Assistant. Answer the user question in a concise and informative manner.",
    ),
    ("human", f"{text}"),
]

if st.button("Summarize"):
    result = llm.invoke(messages)
    st.write(result.content)