import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def Relatorio():
    st.title("Relatorio") 
    bf = pd.read_csv('./BlackFriday.csv')

    marital_true = bf.Age.loc[bf.Marital_Status == 1].value_counts()
    marital_false = bf.Age.loc[bf.Marital_Status == 0].value_counts()

    x1 = marital_true.index
    y1 = marital_true.values

    x2 = marital_false.index
    y2 = marital_false.values

    plt.bar(x1, y1, label='Casados', width=0.4, align='edge')
    plt.bar(x2, y2, label='Não Casados', width=0.4, align='edge')
    plt.legend()
    plt.title('Casados e Não Casados por Idade')


    st.pyplot(plt)
    plt.clf()