import tkinter
import requests

pos_number=input('Ingrese numero de pos: ')
ip_pos=input('Ingrese ip completa de pos: ')
url_way= r"D:\newpos61\POSFILES\LOGS\tlog\POS00"+pos_number
url_pos= rf"\\"+rf"{ip_pos}"+r"\e$\newpos61\posfile\logs"
print(url_way)
print(url_pos)



# hacer menu, pedir pos , fecha y ip completa
# hacer una boton de volver
# una vez que toma la info correcta analizar tpa y anotar evt contarlos y mostrarlos (dar una preview de los eventos)
# hacer seccion de resultados de los test (si tiene o no el resultado obtenido) y poner ok o fail

# url predeterminada way D:\newpos61\POSFILES\LOGS\tlog\POS00
# url predeterminada de las pos e$\newpos61\posfile\logs