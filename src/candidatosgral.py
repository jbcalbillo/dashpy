import streamlit as st
import json

# Título del Dashboard
st.title("Dashboard de Procesos de Selección")

# Cargar el archivo JSON
uploaded_file = st.file_uploader("Sube un archivo JSON", type="json")

if uploaded_file is not None:
    # Leer el archivo JSON
    data = json.load(uploaded_file)
    
    # Verificar si es una lista
    if isinstance(data, list):
        for candidate in data:
            # Mostrar detalles de cada candidato
            st.subheader(f"Detalles del Candidato {candidate.get('idCandidato', 'N/A')}:")
            st.write(f"ID Candidato: {candidate.get('idCandidato', 'N/A')}")
            st.write(f"Fecha de Postulacion: {candidate.get('fechaPostulacion', 'N/A')}")
            st.write(f"Nombre: {candidate.get('nombreCandidato', 'N/A')}")
            st.write(f"Edad: {candidate.get('edad', 'N/A')}")
            st.write(f"Localidad: {candidate.get('localidad', 'N/A')}")
            st.write(f"Genero: {candidate.get('genero', 'N/A')}")
            st.write(f"Empresa Actual: {candidate.get('empresaActual', 'N/A')}")
            st.write(f"Puesto Actual: {candidate.get('puestoActual', 'N/A')}")
            st.write(f"Fecha de Ingreso: {candidate.get('fechaIngreso', 'N/A')}")
            st.write(f"Fecha de Salida: {candidate.get('fechaSalida', 'N/A')}")
            st.write(f"CV: {candidate.get('cv', 'N/A')}")
            st.write(f"Reclutador Asignado: {candidate.get('reclutadorAsignado', 'N/A')}")
            st.write(f"Fuente de Reclutamiento: {candidate.get('fuenteReclutamiento', 'N/A')}")
            st.write(f"Celular: {candidate.get('celular', 'N/A')}")
            st.write(f"Telefono: {candidate.get('telefono', 'N/A')}")
            st.write(f"Correo: {candidate.get('correo', 'N/A')}")
            st.write("---")
    else:
        st.error("El archivo JSON no tiene el formato esperado (una lista de objetos).")
else:
    st.warning("Por favor, sube un archivo JSON para visualizar su contenido.")
