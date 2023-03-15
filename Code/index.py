from flask import Flask,render_template
from ddbb import db
from tkinter.filedialog import askopenfilename, asksaveasfilename
import datetime
# pyright: reportUnboundVariable=false


bases = db()
app=Flask(__name__)

def parseador_log():
            bases[0] # palabras que queremos que esten
            bases[1] # palabras que no queremos que esten
            bases[4] # palabras que queremos marcar
            infile = askopenfilename()
            outfile = asksaveasfilename(defaultextension='.html',initialfile = "contenido_logs",filetypes=[('all files','*.*')])
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
def parseador_errores():
            bases[2]  # palabras que queremos que esten
            bases[3]  # palabras que no queremos que esten
            #bases[5] FUERA DE USO
            bases[6]  # links de confluence
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
                                if any(pharse in palabra for pharse in bases[6]):
                                    marcador = ('<mark>' + palabra + '</mark>')
                                    f[i] = marcador
                                    validador = True
                                    break                                                                           
                            delimited=' '
                            b = delimited.join(f)
                            if validador == True:
                                error = palabra
                                if error in bases[6]:
                                    indice = bases[6].index(palabra) + 1
                                    resultado = bases[6][indice]
                                    outf.write('<h5><a href="'+ resultado +'">' + b + '</a></h5>')
                            else:
                                outf.write('<h5>' + b + '</h5>')             
                outf.write('{% endblock %}')       

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/logs')
def busqueda_log():
    return render_template('logs.html')

@app.route('/resultado')
def resultado_log():
    parseador_log()
    return render_template('contenido_logs.html')

@app.route('/mostrar_log')
def mostrar_log():
    return render_template('contenido_logs.html')


@app.route('/errores')
def busqueda_errores():
    return render_template('errores.html')

@app.route('/resultado_errores')
def resultado_errores():
    parseador_errores()
    return render_template('contenido_errores.html')


@app.route('/mostrar_errores')
def mostrar_errores():
    return render_template('contenido_errores.html')
     
if __name__ == '__main__':
    app.run(port=5017)