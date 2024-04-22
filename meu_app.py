import streamlit as st
import pandas as pd

st.set_page_config(page_title= "Meu primeiro site em PYTHONNNNNNNNNNN")
st.write("Ola mundo, quebrando a rede com sites em PY")
with st.container():#quando quizer separar os conteudos de cada div ou container e editar separadamente

    st.write("Ola mundo, quebrando a rede com sites em PY")# coloque qualer texto simples no site usando esse comando
    st.subheader("")
    st.title(" Dashboard de contratos")
    st.write("Informacoes sobre os contratos fechados")
    st.write("Quer aprender python ? [clique aqui](google.com.br)")

#separando as sessoes do site em containers
@st.cache_data
def carregardados():
    tabela = pd.read_csv('resultados.csv')
    return tabela

with st.container():
    st.write("---")
    qtddias = st.selectbox("Selecione o periodo", ["7d","15d","21d","30d"])
    numdias = int(qtddias.replace("d", ""))
    dados = carregardados()
    dados = dados[-numdias:]
    st.area_chart(dados, x="Data", y="Contratos")
