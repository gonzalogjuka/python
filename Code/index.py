from flask import Flask,render_template
from ddbb import db,base_links
from tkinter.filedialog import askopenfilename, asksaveasfilename


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
                    if not any(phrase in line for phrase in bases[0]):
                        if any(phrase in line for phrase in bases[1]):        
                            f = line.split()
                            del f [0:5]
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
            bases[2] # palabras que queremos que esten
            bases[3] # palabras que no queremos que esten
            bases[5] # palabras para buscar y marcar con sus links de confluence
            bases[6] # links de confluence
            infile = askopenfilename()
            outfile = asksaveasfilename(defaultextension='.html',initialfile = "contenido_errores",filetypes=[('all files','*.*')])
            with open(infile, "r") as inf, open(outfile, "w") as outf:
                outf.write('{% extends "base.html" %} {% block title %} Welcome Morpheus {% endblock %}')
                outf.write('{% block body %}')
                for line in inf:
                    if not any(phrase in line for phrase in bases[2]):
                        if any(phrase in line for phrase in bases[3]):
                            validador = False
                            f = line.split()
                            del f [0:5]
                            for i, palabra in enumerate(f):
                                if any(pharse in palabra for pharse in bases[5]):
                                    marcador = ('<mark>' + palabra + '</mark>')
                                    f[i] = marcador
                                    validador = True
                                    break                                                                                                          
                            delimited=' '
                            b = delimited.join(f)
                            if validador == True:
                                for i,error in enumerate(base_links(bases[6])): # recorro y enemuro
                                    if any(pharse in error for pharse in bases[6]): # verifico si la palabra esta dentro de la base de links
                                        link = base_links(bases[6])[i+1] # sumamos +1 al indice cuando encuentra el error, la entrada consecuente es el link correspondiente al error en cuestion
                                        outf.write('<h5><a href="'+link+'">' + b + '</a></h5>')
                                        break
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
    app.run(debug=True,port=5017)