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

    # Leer el archivo de errores y sugerencias línea por línea
    with open(archivo_errores, 'r') as file:
        lineas_errores = file.readlines()

    # Leer el archivo de origen
    with open(archivo_origen, 'r') as file:
        lineas_codigo = file.readlines()

    # Realizar las correcciones en el código según los errores y sugerencias
    for i, linea_error in enumerate(lineas_errores):
        if linea_error.startswith('Code'):
            partes = linea_error.strip().split(':')
            if len(partes) >= 4:
                archivo = partes[0].strip()
                categoria = partes[3].strip()

                # Obtener la línea y columna del error
                linea = int(partes[1].strip().split('\\')[-1])
                columna = int(partes[2].strip())

                # Realizar acciones en función de la categoría del error
                if categoria == 'Missing module docstring':
                    # Aplicar corrección para el error de falta de docstring del módulo
                    lineas_codigo[linea - 1] = '# Documentación del módulo\n' + lineas_codigo[linea - 1]
                elif categoria == 'Missing class docstring':
                    # Aplicar corrección para el error de falta de docstring de la clase
                    lineas_codigo[linea - 1] = '# Documentación de la clase\n' + lineas_codigo[linea - 1]
                elif categoria == 'Missing function or method docstring':
                    # Aplicar corrección para el error de falta de docstring de la función o método
                    lineas_codigo[linea - 1] = '# Documentación de la función o método\n' + lineas_codigo[linea - 1]
                else:
                    print(f"Categoría de error desconocida en la línea {i + 1} del archivo de errores.")

    # Generar el archivo de salida con las modificaciones realizadas
    archivo_salida = archivo_origen.replace('.py', '_corregido.py')
    with open(archivo_salida, 'w') as file:
        file.writelines(lineas_codigo)

    # Mostrar un mensaje de confirmación al usuario
    print(f"El archivo corregido ha sido generado: {archivo_salida}")


# Llamar a la función principal
corregir_codigo()

