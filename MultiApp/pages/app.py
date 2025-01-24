import streamlit as st

# Crear navegación
pg = st.navigation([
    st.Page("Indicadores_de_calidad_de_vida.py", title="Inicio"),
    st.Page("2_Tabla_de_datos.py", title="Tabla de datos"),
    st.Page("3_Grafica_de_barras.py", title="Gráfica de barras"),
    st.Page("4_Histograma.py", title="Histograma"),
    st.Page("5_Grafica_de_caja.py", title="Gráfico de caja y bigotes"),
    st.Page("6_Grafica_de_dispersion.py", title="Gráfico de dispersión"),
])

pg.run()
