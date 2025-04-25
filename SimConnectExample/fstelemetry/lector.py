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
    return radianes * 180.0 / 3.141592653589793

# Función para leer y procesar la última línea del archivo CSV
def procesar_ultima_linea(archivo):
    while True:
        try:
            # Cargar el archivo CSV nuevamente para obtener los datos más recientes
            df = pd.read_csv(archivo)
            print("✅ Datos cargados desde CSV:")
        except Exception as e_csv:
            print("CSV error:", e_csv)
            return

        # Asegurarse de que la columna 'PLANE_PITCH_DEGREES' exista
        if 'PLANE_PITCH_DEGREES' not in df.columns:
            df['PLANE_PITCH_DEGREES'] = None  # Crear columna si no existe

        # Leer solo la última fila del archivo CSV
        ultima_fila = df.iloc[-1]

        # Convertir los datos a grados (si el valor no es NaN)
        if pd.notna(ultima_fila['PLANE_PITCH_DEGREES*']):
            grados = convertir_a_grados(ultima_fila['PLANE_PITCH_DEGREES*'])
            df.at[df.index[-1], 'PLANE_PITCH_DEGREES'] = grados

        # Imprimir la última fila procesada
        print(f"\nÚltima fila procesada:")
        print(ultima_fila[['time', 'PLANE_PITCH_DEGREES*', 'PLANE_PITCH_DEGREES']])

        time.sleep(1)  # Pausa de 1 segundo antes de leer la siguiente fila

if __name__ == "__main__":
    procesar_ultima_linea(archivo)
