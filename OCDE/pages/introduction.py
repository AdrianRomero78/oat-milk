import streamlit as st
from utils.data_loader import load_data

df = load_data()

st.title("Esperanza de Vida en Países de la OCDE")
st.write("Esta aplicación permite explorar la esperanza de vida en países de la OCDE y otros países.")
st.write("Los datos incluyen mediciones para hombres, mujeres y el total por país a lo largo del tiempo.")
st.write(f"Número total de países en los datos: {df['REF_AREA'].nunique()}")
