from flask import Flask,render_template,request,redirect,url_for
from ddbb import db
import os

bases = db()
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = './Archivos_log'

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/logs')
def busqueda_log():
    return render_template('logs.html') 


@app.route('/errores')
def busqueda_errores():
    bases[0]
    bases[1]
    if request.method == 'POST':
    # obtenemos el archivo del input "archivo"
        f = request.files['archivo']  
        filename = (f.filename)
    # Guardamos el archivo en el directorio "Archivos_log"
        f.save(os.path.join(app.config['UPLOAD_FOLDER']))
    # Retornamos una respuesta satisfactoria
    return render_template('errores.html')

if __name__ == '__main__':
    app.run(debug=True,port=5017)