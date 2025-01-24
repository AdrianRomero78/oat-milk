import streamlit as st
import altair as alt
import pandas as pd

df = pd.read_csv("quality_life_2020.csv", sep=";")

###################################
# Histograma de frecuencias
##################################

st.subheader("Histograma de frecuencias")

# Agregar un selector de enteros para elegir el número de bines

num_bins = st.sidebar.slider("Selecciona el número de bines:", min_value=5, max_value=15, value=8, step=1)

histogram = alt.Chart(df).mark_bar().encode(
    x=alt.X('Quality of Life Index', bin=alt.Bin(maxbins=num_bins)),
    y='count()',
    tooltip='count()'
).properties(
    width=600,
    height=400
)

st.altair_chart(histogram, use_container_width=True)

col1, col2 = st.columns([0.5, 0.5])
with col1:
    st.page_link(label="⬅️ Ir a Gráfica de barras", page="3_Grafica_de_barras.py")
with col2:
    st.page_link(label="Ir a Gráfico de caja y bigotes ➡️", page="5_Grafica_de_caja.py")
