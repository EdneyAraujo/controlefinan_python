import streamlit as st;
import streamlit.components.v1 as components
import pandas as pd
import controllers.LancamentoController as LancamentoController
import models.Lancamentos as lancamento


def Listar():
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
        button_space = col6.empty()
        on_click = button_space.button('Excluir', 'btnExcluir' + str(intem.id))
        