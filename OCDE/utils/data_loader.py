import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    file_path = "OCD.csv"  # Ajusta la ruta según corresponda
    df = pd.read_csv(file_path)
    df = df[['REF_AREA', 'MEASURE', 'SEX', 'TIME_PERIOD', 'OBS_VALUE']]
    df = df[df['MEASURE'] == 'LFEXP']
    return df

# Lista de países OCDE
ocde_countries = {"AUS", "AUT", "BEL", "CAN", "CHL", "COL", "CRI", "CZE", "DNK", "EST",
    "FIN", "FRA", "DEU", "GRC", "HUN", "ISL", "IRL", "ISR", "ITA", "JPN",
    "KOR", "LVA", "LTU", "LUX", "MEX", "NLD", "NZL", "NOR", "POL", "PRT",
    "SVK", "SVN", "ESP", "SWE", "CHE", "TUR", "GBR", "USA"}
