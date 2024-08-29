import streamlit as st
import pandas as pd
import json
import altair as alt

# Título de la vista
st.title("Distribucion de Candidatos por Edad")

# Cargar el archivo JSON
uploaded_file_json = st.file_uploader("Sube un archivo JSON", type="json")

if uploaded_file_json is not None:
    # Leer el archivo JSON
    data = json.load(uploaded_file_json)
    
    # Verificar si es una lista
    if isinstance(data, list):
        # Convertir los datos en un DataFrame
        df = pd.DataFrame(data)
        
        # Filtrar datos válidos
        df = df[df['edad'] > 0]  # Filtra las edades mayores a 0

        # Agrupar por Edad
        grouped = df.groupby('edad').size().reset_index(name='cantidad')
        
        # Mostrar tabla
        st.subheader("Tabla de Candidatos por Edad")
        st.table(grouped)
        
        # Crear un gráfico de barras usando Altair
        chart = alt.Chart(grouped).mark_bar(size=20).encode(
            x=alt.X('edad:O', sort='ascending', axis=alt.Axis(labelAngle=-45, title='Edad')),
            y=alt.Y('cantidad:Q', axis=alt.Axis(title='Cantidad')),
            color=alt.Color('edad:O', legend=None, scale=alt.Scale(scheme='blues')),
            tooltip=['edad', 'cantidad']
        ).properties(
            width=800,
            height=500
        )
        
        # Agregar una capa de texto para mostrar las cantidades sobre cada barra
        text = chart.mark_text(
            align='center',
            baseline='bottom',
            dy=-3,  # Ajuste vertical del texto
            fontSize=12,
            color='white'
        ).encode(
            text='cantidad:Q'
        )
        
        # Superponer las dos capas y aplicar configuraciones estéticas al gráfico final
        final_chart = (chart + text).configure_title(
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
            title='Distribución de Candidatos por Edad'
        )
        
        st.altair_chart(final_chart)
    else:
        st.error("El archivo JSON no tiene el formato esperado (una lista de objetos).")
else:
    st.warning("Por favor, sube un archivo JSON para visualizar el contenido.")
