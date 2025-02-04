import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils.data_loader import load_data, ocde_countries

df = load_data()

st.title("Comparación de Distribuciones")
selected_year = st.radio("Seleccione un año", sorted(df['TIME_PERIOD'].unique(), reverse=True))
df_year = df[df['TIME_PERIOD'] == selected_year]
comparison_type = st.selectbox("Comparar por", ["Género", "Pertenencia a la OCDE"])

plt.figure(figsize=(10, 5))
if comparison_type == "Género":
    sns.boxplot(x='SEX', y='OBS_VALUE', data=df_year)
    plt.xlabel("Género")
else:
    df_year['OCDE'] = df_year['REF_AREA'].apply(lambda x: "OCDE" if x in ocde_countries else "No OCDE")
    sns.boxplot(x='OCDE', y='OBS_VALUE', data=df_year)
    plt.xlabel("Grupo")
plt.ylabel("Esperanza de vida")
st.pyplot(plt)
