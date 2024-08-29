import streamlit as st
import pandas as pd
import json
import altair as alt

# Título de la vista
st.title("Distribucion de Candidatos por Puesto Postulado")

# Cargar el archivo JSON
uploaded_file_json = st.file_uploader("Sube un archivo JSON", type="json")

if uploaded_file_json is not None:
    # Leer el archivo JSON
    data = json.load(uploaded_file_json)
    
    # Verificar si es una lista
    if isinstance(data, list):
        # Convertir los datos en un DataFrame
        df = pd.DataFrame(data)

        # Agrupar por Puesto Postulado
        grouped = df.groupby('puestoPostula').size().reset_index(name='cantidad')
        
        # Mostrar tabla
        st.subheader("Tabla de Candidatos por Puesto Postulado")
        st.table(grouped)
        
        # Crear un gráfico de barras usando Altair
        chart = alt.Chart(grouped).mark_bar().encode(
            x=alt.X('puestoPostula:O', sort='-y'),
            y='cantidad:Q',
            tooltip=['puestoPostula', 'cantidad']
        ).properties(
            width=600,
            height=400
        )
        
        st.altair_chart(chart)
    else:
        st.error("El archivo JSON no tiene el formato esperado (una lista de objetos).")
else:
    st.warning("Por favor, sube un archivo JSON para visualizar el contenido.")
