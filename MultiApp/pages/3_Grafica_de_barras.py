import streamlit as st
import altair as alt
import pandas as pd

###################################
# Gráfico de barras
##################################

df = pd.read_csv("quality_life_2020.csv", sep=";")

st.subheader("Gráfica de barras")

# Agregar un switch que cambie entre los 10 primeros o los últimos 10
# Agregar un switch que permita seleccionar entre orden ascendente o descendente
order = st.sidebar.radio("Ordenar por índice de calidad de vida:", ("Ascendente", "Descendente"))
# Determinar el valor de 'ascending' según el switch
ascending = True if order == "Ascendente" else False

if not ascending:    
    # gráfica de barras con el índice de calidad de vida de los 10 primeros países
    df_bar = df[['Country', 'Quality of Life Index']].iloc[:10].sort_values(by='Quality of Life Index', ascending=False)
else:
    df_bar = df[['Country', 'Quality of Life Index']].iloc[-10:].sort_values(by='Quality of Life Index', ascending=True)

# Crear gráfico de barras usando Altair
chart = alt.Chart(df_bar).mark_bar().encode(
    x=alt.X('Country', sort=None),  # Eje X con nombres de los países
    y='Quality of Life Index'  # Eje Y con los valores numéricos
).properties(
    width=600,  # Ajustar el tamaño del gráfico
    height=400
)

# Mostrar el gráfico en Streamlit
st.altair_chart(chart, use_container_width=True)

col1, col2 = st.columns([0.5, 0.5])
with col1:
    st.page_link(label="⬅️ Ir a Tabla de datos", page="2_Tabla_de_datos.py")
with col2:
    st.page_link(label="Ir a Histograma ➡️", page="4_Histograma.py")
