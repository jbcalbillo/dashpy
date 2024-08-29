import streamlit as st
import json
import pandas as pd
import pydeck as pdk

# Título del Dashboard
st.title("Distribucion de Candidatos por Localidad")

# Cargar el archivo JSON
uploaded_file_json = st.file_uploader("Sube un archivo JSON", type="json")

# Cargar el CSV con coordenadas directamente desde el archivo local
coordenadas_df = pd.read_csv('src/data.csv')

if uploaded_file_json is not None:
    # Leer el archivo JSON
    data = json.load(uploaded_file_json)
    
    # Verificar si es una lista
    if isinstance(data, list):
        # Convertir los datos en un DataFrame para facilitar la manipulación
        df = pd.DataFrame(data)
        
        # Agrupar por Localidad
        grouped = df.groupby('localidad').size().reset_index(name='cantidad')
        
        # Mostrar tabla con la cantidad de candidatos por localidad
        st.subheader("Candidatos por Localidad")
        st.table(grouped)

        # Visualizar en un Mapa
        st.subheader("Mapa de Candidatos por Localidad")
        
        # Mergear el DataFrame agrupado con el DataFrame de coordenadas
        merged_df = pd.merge(grouped, coordenadas_df, left_on="localidad", right_on="NOM_ENT", how="left")

        # Crear una capa de puntos utilizando ScatterplotLayer
        scatter_layer = pdk.Layer(
            "ScatterplotLayer",
            data=merged_df,
            get_position='[LON_DEC, LAT_DEC]',
            get_radius=20000,  # Aumentar el radio para mejor visibilidad
            get_color='[200, 30, 0, 160]',
            pickable=True,
        )

        # Crear una capa de texto utilizando TextLayer para mostrar la cantidad de candidatos
        text_layer = pdk.Layer(
            "TextLayer",
            data=merged_df,
            get_position='[LON_DEC, LAT_DEC]',
            get_text='cantidad',
            get_color='[255, 255, 255, 255]',  # Cambiar el color del texto a blanco para mejor contraste
            get_size=24,  # Ajustar el tamaño del texto para mejor legibilidad
            get_alignment_baseline="'middle'",
        )

        # Configurar la vista inicial del mapa
        view_state = pdk.ViewState(
            latitude=23.634501,
            longitude=-102.552784,
            zoom=5,
            pitch=50,
        )

        # Configurar el estilo del mapa utilizando Mapbox
        map_style = "mapbox://styles/mapbox/light-v10"

        # Mostrar el mapa con las capas de puntos y texto
        st.pydeck_chart(pdk.Deck(
            layers=[scatter_layer, text_layer], 
            initial_view_state=view_state,
            map_style=map_style,
            tooltip={"text": "{localidad}\nCantidad: {cantidad}"}
        ))
    else:
        st.error("El archivo JSON no tiene el formato esperado (una lista de objetos).")
else:
    st.warning("Por favor, sube un archivo JSON para visualizar el contenido.")
