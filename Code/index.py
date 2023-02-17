from flask import Flask,render_template
from ddbb import db
from tkinter.filedialog import askopenfilename, asksaveasfilename


bases = db()
app=Flask(__name__)

def parseador():
            bases[0]
            bases[1]
            infile = askopenfilename()
            outfile = asksaveasfilename(defaultextension='.html',initialfile = "contenido_xml")
            with open(infile, "r") as inf, open(outfile, "w") as outf:
                outf.write('{% extends "base.html" %} {% block title %} Welcome Morpheus {% endblock %}')
                outf.write('{% block body %}')
                for line in inf:
                    if not any(phrase in line for phrase in bases[0]): 
                        if any(phrase in line for phrase in bases[1]):
                            f = line.split()
                            del f [0:5]
                            marcador = f
                            delimited=' '
                            b = delimited.join(f)
                            outf.write('<h5>' + b + '</h5>') # aislar palabras con <mark>
                            for i in marcador:
                                 if i.startswith('Exception:'):
                                      outf.write('<mark></mark>')
                outf.write('{% endblock %}')
                            

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/logs')
def busqueda_log():
    return render_template('logs.html')

@app.route('/resultado')
def resultado():
    parseador()
    return render_template('contenido_xml.html')

@app.route('/mostrar_resultado')
def mostrar_resultado():
    return render_template('contenido_xml.html')

@app.route('/errores')
def busqueda_errores():
    return render_template('errores.html')

     
if __name__ == '__main__':
    app.run(debug=True,port=5017)