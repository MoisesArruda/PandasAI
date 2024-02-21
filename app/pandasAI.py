import pandas as pd
import os
import os
import streamlit as st 
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from pandasai import SmartDataframe
from pandasai.prompts import AbstractPrompt
from gpt import GPTConfig
from langchain.chat_models import AzureChatOpenAI

llm=GPTConfig().create_chat()
print(llm)

file = "data/Lista.xlsx"

df = pd.read_excel(file)
print(df.head())

df= SmartDataframe(df,config={"llm": llm,"verbose":True})

response = df.chat('Qual companhia possui o maior número de usuários ativos?')
print(response)
