import streamlit as st

# Título del Dashboard Principal


# Selector para elegir la vista
option = st.sidebar.selectbox(
    'Selecciona la Vista',
    ('Localidad', 'Edad', 'Puesto Postulado', 'Fuente Reclutamiento', 'Marca', 'Candidatos', 'Data')
)

# Cargar el script correspondiente según la opción seleccionada
if option == 'Localidad':
    exec(open("src/localidad.py").read())
elif option == 'Edad':
    exec(open("src/edad.py").read())
elif option == 'Puesto Postulado':
    exec(open("src/puestoPostula.py").read())
elif option == 'Fuente Reclutamiento':
    exec(open("src/fuenteReclutamiento.py").read())
elif option == 'Marca':
    exec(open("src/marcaPostula.py").read())
elif option == 'Candidatos':
    exec(open("src/candidatosgral.py").read())
elif option == 'Data':
    exec(open("src/data.py").read())

