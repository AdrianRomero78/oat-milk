import streamlit as st
import pandas as pd

###################################
# Tabla de datos
##################################

st.subheader("Tabla de datos")
st.write("Los datos que exploraremos están disponibles en la siguiente tabla:")

df = pd.read_csv("quality_life_2020.csv", sep=";")
st.dataframe(df)

# Agregar botones de navegación
col1, col2 = st.columns([0.5, 0.5])
with col1:
    st.page_link(label="⬅️ Ir a Inicio", page="Indicadores_de_calidad_de_vida.py")
with col2:
    st.page_link(label="Ir a Gráfica de barras ➡️", page="3_Grafica_de_barras.py")