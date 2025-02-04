import streamlit as st
from utils.data_loader import load_data, ocde_countries

df = load_data()

st.title("Resumen Estadístico")
selected_year = st.radio("Seleccione un año", sorted(df['TIME_PERIOD'].unique(), reverse=True))
df_year = df[df['TIME_PERIOD'] == selected_year]
ocde_filter = st.checkbox("Desagrupar por pertenencia a la OCDE")

if ocde_filter:
    df_ocde = df_year[df_year['REF_AREA'].isin(ocde_countries)]
    df_no_ocde = df_year[~df_year['REF_AREA'].isin(ocde_countries)]
    for group_name, data in zip(["OCDE", "No OCDE"], [df_ocde, df_no_ocde]):
        st.subheader(f"Estadísticas - {group_name}")
        st.metric("Promedio", data['OBS_VALUE'].mean())
        st.metric("Desviación estándar", data['OBS_VALUE'].std())
        st.metric("Mínimo", data['OBS_VALUE'].min())
        st.metric("Máximo", data['OBS_VALUE'].max())
else:
    st.metric("Promedio", df_year['OBS_VALUE'].mean())
    st.metric("Desviación estándar", df_year['OBS_VALUE'].std())
    st.metric("Mínimo", df_year['OBS_VALUE'].min())
    st.metric("Máximo", df_year['OBS_VALUE'].max())
