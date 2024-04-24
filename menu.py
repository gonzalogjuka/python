import os
import shutil
import winreg

# Función para liberar memoria virtual
def liberar_memoria_virtual():
    print("Liberando memoria virtual...")
    os.system("wmic os set AutomaticManagedPagefile=True")
    print("Memoria virtual liberada correctamente.")
    input("Presiona Enter para continuar...")

# Función para eliminar archivos temporales de Windows
def eliminar_archivos_temporales():
    print("Eliminando archivos temporales de Windows...")

    # Rutas de los directorios de archivos temporales comunes en Windows
    temp_paths = [
        os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Temp'),
        os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Microsoft', 'Windows', 'INetCache'),
        os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Microsoft', 'Windows', 'Temporary Internet Files'),
        os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Microsoft', 'Windows', 'Caches')
    ]

    total_archivos_eliminados = 0  # Contador para archivos eliminados

    for path in temp_paths:
        # Verificar que la ruta exista antes de eliminar archivos
        if os.path.exists(path):
            print(f"Buscando archivos en la ruta: {path}")  # Debug: imprimir la ruta antes de eliminar archivos
            archivos_eliminados = os.system(f"del /f /q {path}")  # Ejecutar el comando para eliminar archivos
            total_archivos_eliminados += archivos_eliminados

        # Verificar que la ruta exista antes de eliminar archivos y carpetas
        if os.path.exists(path):
            for root, dirs, files in os.walk(path, topdown=False):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        total_archivos_eliminados += 1
                    except Exception as e:
                        print(f"No se pudo eliminar el archivo {file_path}: {e}")
                for dir_name in dirs:
                    dir_path = os.path.join(root, dir_name)
                    try:
                        shutil.rmtree(dir_path)
                        total_archivos_eliminados += 1
                    except Exception as e:
                        print(f"No se pudo eliminar la carpeta {dir_path}: {e}")

    print(f"Se eliminaron {total_archivos_eliminados} archivos y carpetas temporales.")
    print("Archivos y carpetas temporales eliminados correctamente.")
    input("Presiona Enter para continuar...")


# Función para obtener programas de inicio (mantenida para completar el ejemplo)
def obtener_programas_inicio():
    startup_programs = []
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")
    for i in range(winreg.QueryInfoKey(key)[1]):
        try:
            name, value, _ = winreg.EnumValue(key, i)
            startup_programs.append((name, value))
        except EnvironmentError:
            continue
    winreg.CloseKey(key)
    return startup_programs

# Función para mostrar programas de inicio y deshabilitarlos (mantenida para completar el ejemplo)
def mostrar_programas_inicio():
    print("Programas que se ejecutan al inicio:")
    startup_programs = obtener_programas_inicio()

    for index, (name, value) in enumerate(startup_programs, start=1):
        print(f"{index}. {name} - {value}")

    opcion_deshabilitar = int(input("Ingresa el número del programa que deseas deshabilitar (0 para volver al menú): "))

    if opcion_deshabilitar != 0 and opcion_deshabilitar <= len(startup_programs):
        name, value = startup_programs[opcion_deshabilitar - 1]
        print(f"Deshabilitando el programa: {name} - {value}")

        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            winreg.DeleteValue(key, name)
            winreg.CloseKey(key)
            print("Programa deshabilitado correctamente.")
        except Exception as e:
            print(f"Error al deshabilitar el programa: {e}")
    elif opcion_deshabilitar == 0:
        return
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        mostrar_programas_inicio()

# Función principal del menú
def mostrar_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=== Menú ===")
        print("1. Optimizar sistema")
        print("    1.1 Eliminar archivos temporales")
        print("    1.2 Liberar memoria virtual")
        print("2. Mostrar programas de inicio y deshabilitar")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1.1':
            eliminar_archivos_temporales()
        elif opcion == '1.2':
            liberar_memoria_virtual()
        elif opcion == '2':
            mostrar_programas_inicio()
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

    print("Hasta luego.")

# Llamada a la función principal del menú
mostrar_menu()
