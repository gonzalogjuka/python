import os
import winreg

# Función para liberar memoria virtual
def liberar_memoria_virtual():
    print("Liberando memoria virtual...")
    os.system("wmic os set AutomaticManagedPagefile=True")
    print("Memoria virtual liberada correctamente.")

# Función para eliminar archivos temporales de Windows
def eliminar_archivos_temporales():
    print("Eliminando archivos temporales de Windows...")
    
    # Rutas de los directorios de archivos temporales comunes en Windows
    temp_paths = [
        os.path.join(os.environ['SystemRoot'], 'Temp', '*'),
        os.path.join(os.environ['SystemRoot'], 'Prefetch', '*'),
        os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Temp', '*')
    ]

    for path in temp_paths:
        # Verificar que la ruta exista antes de eliminar archivos
        if os.path.exists(path):
            os.system(f"del /f /q {path}")

    print("Archivos temporales eliminados correctamente.")
    

# Función para obtener programas de inicio
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
        print("2. Mostrar programas de inicio y deshabilitar")
        print("0. Salir")
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            print("1. Liberar memoria virtual")
            print("2. Eliminar archivos temporales")
            subopcion = int(input("Selecciona una subopción: "))
            if subopcion == 1:
                liberar_memoria_virtual()
            if subopcion == 2:
                eliminar_archivos_temporales()
            else:
                print("Subopción no válida.")
        elif opcion == 2:
            mostrar_programas_inicio()
        elif opcion == 0:
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

    print("Hasta luego.")

# Llamada a la función principal del menú
mostrar_menu()


