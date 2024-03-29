from tkinter import Tk 
from tkinter.filedialog import askopenfilename, asksaveasfilename
from ddbb import db
import datetime
# pyright: reportUnboundVariable=false

bases = db()
Tk().withdraw()

 # tomar informacion de busqueda de archivos externos
 # y errores con relaciones de confluence y no en diccionarios - Done

 # ordenar vista en HTML y marcar las lineas con errores - Done

 # pintar las linea con referencia a las mismas - Done

 # marcar la linea del error y agregar la etiqueta <a href=""></a>, si lo encuentra
 # confluence con errores (Base de links) que haga macht con la (Base de errores)   - Done
 
 # y cuando inserta la etiqueta <href> pase el link correspondiente, segun el error que encontro en las bases
 # hacer una comprobacion segun palabra de error y devolver un enlace relativo                                  - Done

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
            bases[0] # palabras que queremos que esten
            bases[1] # palabras que no queremos que esten
            bases[4] # base de marcadores
            infile = askopenfilename()
            outfile = asksaveasfilename(defaultextension='.html',initialfile = "resultado_log",filetypes=[('all files','*.*')])
            with open(infile, "r") as inf, open(outfile, "w") as outf:
                outf.write('{% extends "base.html" %} {% block title %} Welcome Morpheus {% endblock %}')
                outf.write('{% block body %}')
                for line in inf:               
                    if not any(phrase in line for phrase in bases[1]): 
                        if any(phrase in line for phrase in bases[0]):                            
                            f = line.split()
                            fecha_hora = f[1]
                            fecha_str, hora_str = fecha_hora.split("T")
                            fecha = datetime.datetime.strptime(fecha_str, "%Y%m%d").strftime("%Y-%m-%d")
                            hora = datetime.datetime.strptime(hora_str[:6], "%H%M%S").strftime("%H:%M:%S")
                            fecha_hora_formateada = fecha + " " + hora
                            f[1] = fecha_hora_formateada
                            del f [2:3]
                            del f [2:4]
                            for i, palabra in enumerate(f):                                                         
                                if any(pharse in palabra for pharse in bases[4]):
                                    marcador = ('<mark>' + palabra + '</mark>')
                                    f[i] = marcador
                                    break                                                                                                                           
                            delimited=' '
                            b = delimited.join(f)    
                            outf.write('<h5>' + b + '</h5>') 
                outf.write('{% endblock %}')                          
def busqueda_errores():
            bases[2]  # palabras que queremos que esten
            bases[3]  # palabras que no queremos que esten
            bases[5]  # links de confluence
            infile = askopenfilename()
            outfile = asksaveasfilename(defaultextension='.html',initialfile = "contenido_errores",filetypes=[('all files','*.*')])
            with open(infile, "r") as inf, open(outfile, "w") as outf:
                outf.write('{% extends "base.html" %} {% block title %} Welcome Morpheus {% endblock %}')
                outf.write('{% block body %}')
                for line in inf:
                    if not any(phrase in line for phrase in bases[3]):
                        if any(phrase in line for phrase in bases[2]):
                            validador = False
                            f = line.split()
                            fecha_hora = f[1]
                            fecha_str, hora_str = fecha_hora.split("T")
                            fecha = datetime.datetime.strptime(fecha_str, "%Y%m%d").strftime("%Y-%m-%d")
                            hora = datetime.datetime.strptime(hora_str[:6], "%H%M%S").strftime("%H:%M:%S")
                            fecha_hora_formateada = fecha + " " + hora
                            f[1] = fecha_hora_formateada
                            del f [2:3]
                            del f [2:4]
                            for i, palabra in enumerate(f):
                                if any(pharse in palabra for pharse in bases[5]):
                                    marcador = ('<mark>' + palabra + '</mark>')
                                    f[i] = marcador
                                    validador = True
                                    break                                                                                                          
                            delimited=' '
                            b = delimited.join(f)
                            if validador == True:                                       
                                error = palabra
                                if error in bases[5]:
                                    indice = bases[5].index(palabra) + 1
                                    resultado = bases[5][indice] #incide ok
                                    outf.write('<h5><a href="'+ resultado +'">' + b + '</a></h5>')                                                             
                            else:
                                outf.write('<h5>' + b + '</h5>')                            
                outf.write('{% endblock %}')  

def salir_menu():
     print('Volviendo')
def salir():
        exit() 
menu_principal()