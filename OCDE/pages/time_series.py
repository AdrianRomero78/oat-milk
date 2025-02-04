import streamlit as st
import matplotlib.pyplot as plt
from utils.data_loader import load_data

df = load_data()

st.title("Evolución Temporal de la Esperanza de Vida")
selected_countries = st.multiselect("Seleccione países", df['REF_AREA'].unique(), default=["MEX", "USA"])
gender_filter = st.radio("Filtrar por género", ["Total", "Hombres", "Mujeres"])
gender_map = {"Total": "_T", "Hombres": "M", "Mujeres": "F"}
df_filtered = df[df['REF_AREA'].isin(selected_countries) & (df['SEX'] == gender_map[gender_filter])]

plt.figure(figsize=(10, 5))
for country in selected_countries:
    country_data = df_filtered[df_filtered['REF_AREA'] == country]
    plt.plot(country_data['TIME_PERIOD'], country_data['OBS_VALUE'], marker='o', label=country)
plt.xlabel("Año")
plt.ylabel("Esperanza de vida")
plt.legend()
st.pyplot(plt)
