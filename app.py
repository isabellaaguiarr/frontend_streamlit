import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Diretório base do arquivo atual
caminho = Path(__file__).resolve().parent

# streamlit run app.py no terminal!
st.title("Meu primeiro dashboard!")
st.header("Esse é o corpo do texto.")
st.markdown(
    '''
    # Titulo
    ## Subtitulo
    ### Corpo do texto
    '''
)

# Carregando o CSV uma única vez no início
df = pd.read_csv(caminho / "data" / "planilhao.csv")  # Usando Pathlib para criar o caminho

# Criando as abas
abas = st.tabs(["Botão", "Radio", "Dataframe", "Gráfico"])

# Aba 1: Botão
with abas[0]:
   if st.button("enter"):
      st.text("Este é o button")

# Aba 2: Radio
with abas[1]:
   opcao = st.radio(
       "Escolha a opção:",
       ("Azul", "Amarelo", "Rosa")
   )

   if opcao == "Azul":
       st.info("Sua cor é o azul!")
   elif opcao == "Amarelo":
       st.warning("Sua cor é o amarelo!")
   else:
       st.error("Sua cor é o rosa!")

# Aba 3: Dataframe
with abas[2]:
   st.dataframe(df)

# Aba 4: Gráfico

