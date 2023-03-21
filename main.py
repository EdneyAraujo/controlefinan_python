from os import write
import streamlit as st;
import streamlit.components.v1 as components
import pandas as pd
import controllers.LancamentoController as LancamentoController
import models.Lancamentos as lancamento
import Pages.Lancamentos.Incluir as PagesIncluirLancanto
import Pages.Lancamentos.Listar as PagesListar
import Pages.Lancamentos.relatorio as PageRel


with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

st.sidebar.title("MENU")
page_cliente = st.sidebar.selectbox('',['Incluir','Consultar','Relatorio'] )


if page_cliente == 'Incluir':
    PagesIncluirLancanto.Incluir()

if page_cliente == 'Consultar':
    PagesListar.Listar()

if page_cliente == 'Relatorio':
    PageRel.Relatorio()