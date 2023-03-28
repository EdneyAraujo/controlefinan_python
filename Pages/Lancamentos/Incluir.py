import streamlit as st;
import controllers.LancamentoController as LancamentoController
import models.Lancamentos as lancamento

def Incluir():
    st.title("Incluir Lancamentos")
    
    
    with st.form(key="incluir_cliente"):
        input_descricao = st.text_input(label="Descrição")
        input_descricao = st.text_input(label="DATA")
        input_valor = st.number_input("Insira o Valor")    
        input_tipo = st.selectbox("SELECIONE O TIPO LANÇAMENTO", options=["RECEITA","DESPESA"])
        input_categoria = st.selectbox("SELECIONE A CATEGORIA", options=["MORADIA","LAZER","ESTUDOS"])
        input_button_submit = st.form_submit_button("Enviar")
    if input_button_submit:
        LancamentoController.Incluir(lancamento.Lancamentos(0, input_descricao, input_valor, input_tipo, input_categoria))
        st.success("LANÇAMENTO CADASTRADO COM SUCESSO")