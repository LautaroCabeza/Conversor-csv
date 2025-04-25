import sys
import pandas as pd
import os
import time

if len(sys.argv) < 2:
    print("Uso: python lector.py <archivo.csv>")
    sys.exit(1)

archivo = sys.argv[1]

# Mostrar la ruta absoluta para verificar
ruta_completa = os.path.abspath(archivo)
print(f"Intentando abrir: {ruta_completa}")

# Función para convertir radianes a grados
def convertir_a_grados(radianes):
    return radianes * 180 / 3.141592653589793

while True:
    try:
        # Cargar el archivo CSV
        df = pd.read_csv(archivo)
        
        # Realizar la conversión de radianes a grados en la columna correspondiente
        if 'PLANE_PITCH_DEGREES*' in df.columns:
            df['PLANE_PITCH_DEGREES'] = df['PLANE_PITCH_DEGREES*'].apply(convertir_a_grados)
        
        # Imprimir solo las últimas 5 filas (puedes ajustarlo a tu preferencia)
        print("\nÚltimos 5 registros:")
        print(df.tail(5))
        
        print("✅ Conversión de radianes a grados realizada correctamente")
        
    except Exception as e_csv:
        print("CSV error:", e_csv)
    
    # Esperar 5 segundos antes de la siguiente actualización (puedes ajustar el tiempo)
    time.sleep(5)
