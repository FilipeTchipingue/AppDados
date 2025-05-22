import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sbn
import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(page_title="Reporting de Vendas Python",page_icon=":bar_chart:",layout="wide",initial_sidebar_state="collapsed")
st.title("Reporting Vendas")

BaseDados = pd.read_csv(r"C:\Users\filipe.tchipingue\OneDrive - Wayfield\Ambiente de Trabalho\BasePythn\Sales.csv")
opt = st.sidebar.multiselect("Selecione",["Dados","Analise Exploratória","Grafico"])
sele =st.selectbox("Selecione o Categoria:",options=BaseDados["Category"].unique())
Basefiltrada = BaseDados.loc[BaseDados["Category"]==sele]

#fig =px.bar(data_frame=DadosAgrupados, y="Amount",x="Category",color="Category",text_auto=True)
baseAgrupada = Basefiltrada.groupby(["Year-Month","State"])["Amount"].sum().reset_index()
baseAgrupada2 = Basefiltrada.groupby(["PaymentMode","State"])["Amount"].sum().reset_index()

coluna1,coluna2,coluna3,coluna4 = st.columns(4)
with coluna1:
    st.metric("Total de Vendas",f"{Basefiltrada["Amount"].sum():,.2f} AOA")
with coluna2:
    st.metric("Média de Vendas",f"{Basefiltrada["Amount"].mean():,.2f} AOA")
with coluna3:
    st.metric("Maior Venda",f"{Basefiltrada["Amount"].max():,.2f} AOA")
with coluna4:
    st.metric("Ménor Venda",f"{Basefiltrada["Amount"].min():,.2f} AOA")
st.divider()

col1,col2 = st.columns([0.5,0.5])
with col1:
    figura1 = px.line(x="Year-Month",y="Amount",color="State",data_frame=baseAgrupada,title="Evolução de Vendas")

    st.plotly_chart(figura1,use_container_width=True)
with col2:
    figura2 = px.bar(x="Year-Month",y="Amount",color="State",data_frame=baseAgrupada,title="Evolução de Vendas")

    st.plotly_chart(figura2,use_container_width=True)
co1,co2=st.columns(2)
with co1:
    fi1=px.pie(data_frame=baseAgrupada,names="State",values="Amount",title="Peso por Estado")
    st.plotly_chart(fi1,use_container_width=True)
with co2:
    fig2=px.box(data_frame=baseAgrupada2,x="PaymentMode",y="Amount",title="Distribuição por estado")
    st.plotly_chart(fig2,use_container_width=True)
    