import streamlit as st

# Crear navegación con páginas específicas
pg = st.navigation([
    st.Page("pages/introduction.py", title="Introducción"),
    st.Page("pages/statistics.py", title="Resumen Estadístico"),
    st.Page("pages/distribution.py", title="Visualización I"),
    st.Page("pages/time_series.py", title="Visualización II"),
])

# Ejecutar la navegación
pg.run()