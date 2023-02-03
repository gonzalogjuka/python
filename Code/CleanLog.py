"""
#Version Vieja

from tkinter import Tk 
from tkinter.filedialog import askopenfilename, asksaveasfilename
# pyright: reportUnboundVariable=false

log=["DEBUG","INFO","WARNING"]
not_log = ["#####","<?xml","npreMemory.c{DEP}","npDrvPublEVT","npreFindClose","SendRecvTCPMsg","npreMsg.c{DEP}@2922","npreControlProcess.c{DEP}@149","npreOSItf.c{DEP}@796","npreOSItf.c{DEP}@254","ERROR","WARNING","N E W"]
errors = ["ERROR","N E W ","WARNING","FATAL"]
not_erros= ["ERROR_LOG","Error de comunicacion","Error executing command","npreFindClose","SendRecvTCPMsg resource","InsertResource resource","WARNING_LOG","COD0028","npreMsg2_SendRecvEx","GetResource:","Configuration parameter","ChangeItemPriceBySaleType","PosShowPrice","PosDoTryGrillEnd","cPosCheckPromotedOrder","PosConvertProduct","The Offers Server took more","sharpmessaging.cpp{DEP}@225","npreMemory.c","npDrvPublEVT.c"]

Tk().withdraw()
pregunta = input('Que accion queres tomar?: \n\t1- Resumir Log\n\t2- Busqueda de solo errores\n\t3- Salir\n')
if pregunta == '3':exit()
if pregunta == '1':
            infile = askopenfilename()
            outfile = asksaveasfilename()
            with open(infile, "r") as inf, open(outfile, "w") as outf:
                for line in inf:
                    if not any(phrase in line for phrase in not_log): 
                        if any(phrase in line for phrase in log):       
                            f = line.split()  
                            del f [0:5]
                            delimited=' '
                            b = delimited.join(f)          
                            outf.write(b + '\n')  
elif pregunta == '2':
            infile = askopenfilename()
            error = asksaveasfilename()
            with open(infile, "r") as inf, open(error, "w")as errores:
                for line in inf:
                    if any(phrase in line for phrase in errors):
                            if not any(phrase in line for phrase in not_erros):  
                                f = line.split()
                                del f [0:5]
                                delimited=' '
                                b = delimited.join(f)
                                errores.write(b + '\n')
else:
      print('Por favor,elegir una opcion valida')
"""     

from tkinter import Tk 
from tkinter.filedialog import askopenfilename, asksaveasfilename
# pyright: reportUnboundVariable=false

log=["DEBUG","INFO","WARNING"]
not_log = ["#####","<?xml","npreMemory.c{DEP}","npDrvPublEVT","npreFindClose","SendRecvTCPMsg","npreMsg.c{DEP}@2922","npreControlProcess.c{DEP}@149","npreOSItf.c{DEP}@796","npreOSItf.c{DEP}@254","ERROR","WARNING","N E W"]
errors = ["ERROR","N E W ","WARNING","FATAL"]
not_erros= ["ERROR_LOG","Error de comunicacion","Error executing command","npreFindClose","SendRecvTCPMsg resource","InsertResource resource","WARNING_LOG","COD0028","npreMsg2_SendRecvEx","GetResource:","Configuration parameter","ChangeItemPriceBySaleType","PosShowPrice","PosDoTryGrillEnd","cPosCheckPromotedOrder","PosConvertProduct","The Offers Server took more","sharpmessaging.cpp{DEP}@225","npreMemory.c","npDrvPublEVT.c"]
Tk().withdraw()

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
        '2': ('Buscar de errores >>',sub_menu),
        '3': ('Salir', salir)
    }
    generar_menu('Menu principal',opciones, '3')
def sub_menu():
     opciones={
          '1':('Solo errores', busqueda_errores),
          '2':('Errores con warnings', ),
          '3':('Volver al menu principal', salir_menu)
     }

     generar_menu('Submenu',opciones,'3')
def busqueda_logs():
            infile = askopenfilename()
            outfile = asksaveasfilename()
            with open(infile, "r") as inf, open(outfile, "w") as outf:
                for line in inf:
                    if not any(phrase in line for phrase in not_log): 
                        if any(phrase in line for phrase in log):       
                            f = line.split()  
                            del f [0:5]
                            delimited=' '
                            b = delimited.join(f)          
                            outf.write(b + '\n')   
def busqueda_errores():
            infile = askopenfilename()
            error = asksaveasfilename()
            with open(infile, "r") as inf, open(error, "w")as errores:
                for line in inf:
                    if any(phrase in line for phrase in errors):
                            if not any(phrase in line for phrase in not_erros):  
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