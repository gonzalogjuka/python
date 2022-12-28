import tkinter as tk
import tkinter.filedialog as fd

# Creamos la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Cargar archivo XML")

# Creamos un botón para seleccionar el archivo
boton_archivo = tk.Button(ventana, text="Seleccionar archivo", command=lambda: seleccionar_archivo())
boton_archivo.pack()

# Creamos una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

def seleccionar_archivo():
  # Esta función se ejecuta cuando se hace clic en el botón "Seleccionar archivo"
  # y permite al usuario seleccionar un archivo a través de la GUI
  archivo = fd.askopenfilename(filetypes=[("Archivos XML", "*.xml")])
  if archivo:
    # Mostramos el nombre del archivo seleccionado en la etiqueta
    etiqueta_resultado.config(text=f"Archivo seleccionado: {archivo}")
    # Cerramos la ventana principal y abrimos una nueva ventana con tres botones
    ventana.destroy()
    menu(archivo)

def menu(archivo):
  # Esta función crea una nueva ventana con tres botones
  ventana_menu = tk.Tk()
  ventana_menu.title("Menú de opciones")

  def ejemplo1():
    print("Has seleccionado la opción de nuevo menu")
    ventana_menu.destroy()
    menu2()

  def ejemplo2():
    print("Has seleccionado la opción ejemplo2")

  def ejemplo3():
    print("Has seleccionado la opción ejemplo3")

  boton_ejemplo1 = tk.Button(ventana_menu, text="Nuevo Menu", command=ejemplo1)
  boton_ejemplo1.pack()
  boton_ejemplo2 = tk.Button(ventana_menu, text="Ejemplo2", command=ejemplo2)
  boton_ejemplo2.pack()
  boton_ejemplo3 = tk.Button(ventana_menu, text="Ejemplo3", command=ejemplo3)
  boton_ejemplo3.pack()

def menu2():
  # Esta función crea una nueva ventana con tres botones
  menu2 = tk.Tk()
  menu2.title("Nuevo Menu") 

  def new_option():
    print("Has seleccionado la opción ejemplo2")
    
  boton_ejemplo= tk.Button(menu2, text="Nuevo Menu 2", command=new_option)
  boton_ejemplo.pack()
  