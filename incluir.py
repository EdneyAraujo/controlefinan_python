import streamlit as st;

with st.form(key="incluir_cliente"):
    input_name = st.text_input(label="Inserir Lançamaneto")
    input_age = st.number_input("Insira o Valor")
    input_button_submit = st.form_submit_button("Enviar")