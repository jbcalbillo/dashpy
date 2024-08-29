import json
import random

def asignar_edades_aleatorias(archivo_json):
    # Cargar el archivo JSON
    with open(archivo_json, 'r', encoding='utf-8') as file:
        datos = json.load(file)

    # Verificar si es una lista de registros o un solo registro
    if isinstance(datos, list):
        for registro in datos:
            registro['edad'] = random.randint(18, 60)
    else:
        datos['edad'] = random.randint(18, 60)

    # Guardar los cambios en el archivo JSON
    with open(archivo_json, 'w', encoding='utf-8') as file:
        json.dump(datos, file, ensure_ascii=False, indent=4)

    print(f"Edades asignadas correctamente en {archivo_json}.")

# Uso de la función
asignar_edades_aleatorias('src/candidatos2024.json')
