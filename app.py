import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from pathlib import Path
caminho = str(Path(__file__).resolve().parent)

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
# caminho = "C:\\Users\\isabe\\Documents\\PROJETOS\\atividadesSala\\frontend"
df = pd.read_csv(caminho + "\\data\\planilhao.csv")

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
with abas[3]:
   # Filtrando os dados
   filter = df['ticker'].isin(["RNEW4", "KEPL3", "PETR4", "EPAR3", "UNIP6", "BRAP4", "TASA4", "GOAU4", "RSUL4", "GGBR4"])
   df_bar = df.loc[filter, ["ticker", "roe"]]

   # Valores de x e y
   x = df_bar['ticker'].values
   y = df_bar['roe'].values

   # Lista de cores personalizadas (uma para cada barra)
   colors = ['#ADD8E6', '#98FF98', '#FFFACD', '#FFC0CB', '#E6E6FA', '#FF7F50', '#D3D3D3', '#FFD700', '#008080', '#002300']

   # Criando o gráfico de barras
   fig, ax = plt.subplots()
   ax.bar(x, y, color=colors)

   # Exibindo o gráfico no Streamlit
   st.pyplot(fig)
