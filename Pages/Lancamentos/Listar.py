import streamlit as st;
import streamlit.components.v1 as components
import pandas as pd
import controllers.LancamentoController as LancamentoController
import models.Lancamentos as lancamento

def Listar():
    st.title("Lançamentos")
    colms = st.columns((1, 2, 1, 1, 1,2))
    campos = ['id','Descricao', 'Valor', 'Tipo', 'Categoria','Excluir']
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)

    for intem in LancamentoController.SelecionarTodos():
        col1, col2, col3, col4, col5, col6 = st.columns((1, 2, 1, 1, 1,2))
        col1.write(intem.id)
        col2.write(intem.descricao)
        col3.write(intem.valor)
        col4.write(intem.tipo)
        col5.write(intem.categoria)
        button_space_excluir = col6.empty()
        on_click_excluir = button_space_excluir.button('Excluir', 'btnExcluir' + str(intem.id))
        
        if on_click_excluir:
            LancamentoController.Excluir(intem.id)
            button_space_excluir.button('Excluido')