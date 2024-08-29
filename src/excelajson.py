import pandas as pd
import json

# Cargar el archivo Excel
df = pd.read_excel('archivo.xlsx')

# Iterar sobre las columnas y convertir Timestamps a cadenas
for col in df.columns:
    if df[col].dtype == 'datetime64[ns]':  # Verificar si la columna es de tipo datetime
        df[col] = df[col].dt.strftime('%Y-%m-%d %H:%M:%S')  # Formatear según sea necesario

# Reemplazar celdas vacías con 0
df = df.fillna(0)

# Convertir DataFrame a diccionario
data_dict = df.to_dict(orient='records')

# Convertir diccionario a JSON
json_data = json.dumps(data_dict, indent=4, ensure_ascii=False)

# Guardar JSON en un archivo
with open('archivo.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

print("Archivo convertido a JSON y guardado como 'archivo.json'")
