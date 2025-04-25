import csv
import time

ruta_archivo = 'datos.csv'

try:
    with open(ruta_archivo, newline='', mode='r') as archivo:
        lector = csv.reader(archivo)
        
        # Leer encabezado y verificar columnas
        encabezado = next(lector)
        if 'time' not in encabezado or 'PLANE_PITCH_DEGREES' not in encabezado:
            print("❌ Encabezado inválido. Se esperaban las columnas 'time' y 'PLANE_PITCH_DEGREES'.")
        else:
            # Índices seguros por nombre
            i_time = encabezado.index('time')
            i_pitch = encabezado.index('PLANE_PITCH_DEGREES')

            # Bucle para leer líneas continuamente
            while True:
                fila = next(lector, None)
                if fila is None:
                    time.sleep(0.5)  # Esperar medio segundo para no sobrecargar el procesamiento
                    continue  # Esperar a que lleguen nuevas filas

                if len(fila) < 2:
                    print(f"❌ Fila malformada o incompleta: {fila}")
                    continue

                try:
                    timestamp = float(fila[i_time])
                    pitch = float(fila[i_pitch])
                    print(f"⏱ {timestamp:.2f} | 🎯 Pitch°: {pitch:.6f} °")
                except ValueError:
                    print(f"❌ Error de conversión en fila: {fila}")
except FileNotFoundError:
    print(f"❌ No se encontró el archivo en la ruta: {ruta_archivo}")
