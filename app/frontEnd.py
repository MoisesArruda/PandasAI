import streamlit as st
from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
from read_excel import create_awnser
from streamlit_chat import message
import pandas as pd
from pandasai import SmartDataframe

st.set_page_config(page_title="Chatbot", page_icon="📋",layout="wide")

with st.sidebar:
    st.title('CHAT-EMPRESARIAL :books:')
    st.warning('LISTA DAS PLANILHAS – Nº 01/2024')

    df = pd.read_excel("data/Lista.xlsx")
    st.dataframe(df.head(20))

st.title("Iniciando conversa com o ChatBot... ")

if "messages" not in st.session_state.keys():
    st.session_state.messages=[
        {"role":"assistant","content": "Olá! Faça sua pergunta referente ao documento armazenado."}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_prompt = st.chat_input()

if user_prompt is not None:
    st.session_state.messages.append(
        {"role":"user","content":user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response=create_awnser(query=user_prompt)
            st.write(ai_response)
    new_ai_message = {"role":"assistant","content":ai_response}
    st.session_state.messages.append(new_ai_message)