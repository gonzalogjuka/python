import tkinter
import requests

opcion = input('Ingrese una opcion: ')

# hacer menu, pedir pos , fecha y ip completa
if opcion == 1:
    pos_number=input('Ingrese numero de pos: ')
    url_way= r"D:\newpos61\POSFILES\LOGS\tlog\POS00"+pos_number
    print('El numero de pos es el siguiente' + url_way)
elif opcion == 2:
    ip_pos=input('Ingrese ip completa de pos: ')
    url_pos= rf"\\"+rf"{ip_pos}"+r"\e$\newpos61\posfile\logs"
    print('La ip elegida es: ' + ip_pos)
#expression cannot be asigment target pylance

# hacer una boton de volver
# una vez que toma la info correcta analizar tpa y anotar evt contarlos y mostrarlos (dar una preview de los eventos)
# hacer seccion de resultados de los test (si tiene o no el resultado obtenido) y poner ok o fail

# url predeterminada way D:\newpos61\POSFILES\LOGS\tlog\POS00
# url predeterminada de las pos e$\newpos61\posfile\logs