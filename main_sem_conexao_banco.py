from os import write
import streamlit as st;

st.title("Incluir Lancamentos")
st.sidebar.title("MENU")
page_cliente = st.sidebar.selectbox('',['Incluir','Consultar'] )

if page_cliente == 'Consultar':
    st.title('Incluir Lancamentos')
    costumerList = []

with st.form(key="incluir_cliente"):
    input_name = st.text_input(label="Inserir Lançamaneto")
    input_age = st.number_input("Insira o Valor")
    input_ocupation = st.selectbox("SELECIONE O TIPO LANÇAMENTO", options=["Receita","Despesa"])
    input_ocupation2 = st.selectbox("SELECIONE A CATEGORIA", options=["MORADIA","LAZER","ESTUDOS"])
    input_button_submit = st.form_submit_button("Enviar")

if input_button_submit:
    st.write(f'Nome: {input_name}')
    st.write(f'Idade: {input_age}')
    st.write(f'Tipo: {input_ocupation}')
    st.write(f'Categoria: {input_ocupation2}')