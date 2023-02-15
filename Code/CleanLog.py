from tkinter import Tk 
from tkinter.filedialog import askopenfilename, asksaveasfilename
from ddbb import db
# pyright: reportUnboundVariable=false

bases = db()
Tk().withdraw()

 # tomar informacion de busqueda de archivos externos
 # y errores con relaciones de confluence y no en diccionarios - Done

 # ordenar vista en HTML y marcar las lineas con errores - Done

 # pintar las linea con referencia a las mismas

def mostrar_menu(nombre,opciones):
   print(f'# {nombre}. Seleccione una opción:')
   for clave in sorted(opciones):
    print(f' {clave}) {opciones[clave][0]}')
def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a
def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()
def generar_menu(nombre,opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(nombre, opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()
def menu_principal():
    opciones = {
        '1': ('Resumir Log', busqueda_logs),
        '2': ('Buscar de errores >>',sub_menu_errores),
        '3': ('Salir', salir)
    }
    generar_menu('Menu principal',opciones, '3')
def sub_menu_errores():
     opciones={
          '1':('Solo errores', busqueda_errores),
          '2':('Errores con warnings (En Desarrollo,no usar)', ),
          '3':('Volver al menu principal', salir_menu)
     }

     generar_menu('Submenu',opciones,'3')
def busqueda_logs():
            bases[0]
            bases[1]
            infile = askopenfilename()
            outfile = asksaveasfilename(defaultextension='.html',initialfile = "resultado_log",filetypes=[('all files','*.*')])
            with open(infile, "r") as inf, open(outfile, "w") as outf:
                for line in inf:
                    if not any(phrase in line for phrase in bases[0]): 
                        if any(phrase in line for phrase in bases[1]):       
                            f = line.split()  
                            del f [0:5]
                            delimited=' '
                            b = delimited.join(f)       
                            outf.write(b + '\n')                           

def busqueda_errores():
            bases[2]
            bases[3]
            infile = askopenfilename()
            error = asksaveasfilename(defaultextension='.html',initialfile = "resultado_errores",filetypes=[('all files','*.*')])
            with open(infile, "r") as inf, open(error, "w")as errores:
                for line in inf:
                    if any(phrase in line for phrase in bases[2]):
                            if not any(phrase in line for phrase in bases[3]):  
                                f = line.split()
                                del f [0:5]
                                delimited=' '
                                b = delimited.join(f)
                                errores.write(b + '\n')
def salir_menu():
     print('Volviendo')
def salir():
        exit() 
menu_principal()