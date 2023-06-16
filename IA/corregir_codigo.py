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

    # Diccionario para almacenar las acciones a ejecutar según el disparador (categoría del error)
    acciones = {
        'Missing module docstring': corregir_falta_docstring_modulo,
        'Missing class docstring': corregir_falta_docstring_clase,
        'Missing function or method docstring': corregir_falta_docstring_funcion,
        # Agrega más disparadores y funciones de corrección según sea necesario
    }

    # Realizar las correcciones en el código según los errores y sugerencias
    for linea_error in lineas_errores:
        if linea_error.startswith('Code'):
            partes = linea_error.strip().split(':')
            if len(partes) >= 4:
                categoria = partes[3].strip()

                # Verificar si la categoría del error tiene una acción asociada en el diccionario
                if categoria in acciones:
                    # Obtener la línea y columna del error
                    linea = int(partes[1].strip().split('\\')[-1])
                    columna = int(partes[2].strip())

                    # Llamar a la función de corrección asociada a la categoría del error
                    acciones[categoria](lineas_codigo, linea, columna)

                else:
                    print(f"Categoría de error desconocida en el archivo de errores: {categoria}")

    # Generar el archivo de salida con las modificaciones realizadas
    archivo_salida = archivo_origen.replace('.py', '_corregido.py')
    with open(archivo_salida, 'w') as file:
        file.writelines(lineas_codigo)

    # Mostrar un mensaje de confirmación al usuario
    print(f"El archivo corregido ha sido generado: {archivo_salida}")

def corregir_falta_docstring_modulo(lineas_codigo, linea, columna):
    # Aplicar corrección para el error de falta de docstring del módulo
    lineas_codigo[linea - 1] = '# Documentación del módulo\n' + lineas_codigo[linea - 1]

def corregir_falta_docstring_clase(lineas_codigo, linea, columna):
    # Aplicar corrección para el error de falta de docstring de la clase
    lineas_codigo[linea - 1] = '# Documentación de la clase\n' + lineas_codigo[linea - 1]

def corregir_falta_docstring_funcion(lineas_codigo, linea, columna):
    # Aplicar corrección para el error de falta de docstring de la función o método
    lineas_codigo[linea - 1] = '# Documentación de la función o método\n' + lineas_codigo[linea - 1]

# Llamar a la función principal
corregir_codigo()


