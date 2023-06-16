from tkinter import Tk, filedialog

def solicitar_archivo(mensaje):
    root = Tk()
    root.withdraw()

    # Mostrar el cuadro de diálogo para seleccionar el archivo
    archivo = filedialog.askopenfilename(title=mensaje)

    return archivo

def corregir_codigo():
    # Solicitar al usuario los archivos de origen y los archivos de errores y sugerencias
    archivo_origen = solicitar_archivo("Seleccione el archivo de origen en Python")
    archivo_errores = solicitar_archivo("Seleccione el archivo de errores y sugerencias")

    # Leer el archivo de errores y sugerencias
    with open(archivo_errores, 'r') as file:
        lineas_errores = file.readlines()

    # Leer el archivo de origen
    with open(archivo_origen, 'r') as file:
        lineas_codigo = file.readlines()

    # Realizar las correcciones en el código según los errores y sugerencias
    for linea_error in lineas_errores:
        partes = linea_error.strip().split(';')
        if len(partes) > 1:
            try:
                linea = int(partes[0]) - 1

                # Aplicar la corrección a la línea correspondiente en el código
                lineas_codigo[linea] = partes[1] + '\n'
            except ValueError:
                print("Error: El número de línea no es válido en la línea:", linea_error)
        else:
            print("Error: La línea no está en el formato esperado:", linea_error)

    # Generar el archivo de salida con las modificaciones realizadas
    archivo_salida = archivo_origen.replace('.py', '_corregido.py')
    with open(archivo_salida, 'w') as file:
        file.writelines(lineas_codigo)

    # Mostrar un mensaje de confirmación al usuario
    print(f"El archivo corregido ha sido generado: {archivo_salida}")

# Llamar a la función principal
corregir_codigo()

