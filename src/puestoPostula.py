import streamlit as st
import pandas as pd
import json
import altair as alt

# Título de la vista
st.title("Distribucion de Candidatos por Postulación a Puestos y Marca")

# Cargar el archivo JSON
uploaded_file_json = st.file_uploader("Sube un archivo JSON", type="json")

if uploaded_file_json is not None:
    # Leer el archivo JSON
    data = json.load(uploaded_file_json)
    
    # Verificar si es una lista
    if isinstance(data, list):
        # Convertir los datos en un DataFrame
        df = pd.DataFrame(data)
        
        # Agrupar por Puesto Postulado y Marca Postulada
        grouped = df.groupby(['puestoPostula', 'marcaPostula']).size().reset_index(name='cantidad')
        
        # Mostrar tabla
        st.subheader("Tabla de Candidatos por Postulación a Puestos y Marca")
        st.table(grouped)
        
        # Crear un gráfico de barras apilado usando Altair
        chart = alt.Chart(grouped).mark_bar().encode(
            x=alt.X('puestoPostula:O', sort='-y', axis=alt.Axis(labelAngle=-45, title='Puesto Postulado')),
            y=alt.Y('cantidad:Q', axis=alt.Axis(title='Cantidad')),
            color=alt.Color('marcaPostula:N', legend=alt.Legend(title="Marca Postulada")),
            tooltip=['puestoPostula', 'marcaPostula', 'cantidad']
        ).properties(
            width=800,
            height=500
        )
        
        # Aplicar configuraciones estéticas al gráfico final
        final_chart = chart.configure_title(
            fontSize=20,
            anchor='start',
            color='gray'
        ).configure_axis(
            labelFontSize=12,
            titleFontSize=14,
            labelColor='gray',
            titleColor='gray'
        ).configure_view(
            strokeWidth=0
        ).properties(
            title='Distribucion de Candidatos por Postulación a Puestos y Marca'
        )
        
        st.altair_chart(final_chart)
    else:
        st.error("El archivo JSON no tiene el formato esperado (una lista de objetos).")
else:
    st.warning("Por favor, sube un archivo JSON para visualizar el contenido.")
