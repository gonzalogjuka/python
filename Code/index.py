from flask import Flask,render_template,request,redirect,url_for
from ddbb import db
from tkinter.filedialog import askopenfilename, asksaveasfilename
from werkzeug.utils import secure_filename


bases = db()
app=Flask(__name__)


@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/logs',methods=['GET', 'POST'])
def busqueda_log():
            bases[0]
            bases[1]
            if request.method == 'POST':
                file = request.files['the_file']
                x = file.save(f"/saver/Resultado.html")
            return render_template('logs.html',base_0=bases[0],base_1=bases[1],info = x) # les pasamos las bases al template

@app.route('/resultado')
def resultado():
            #mostrar info aca con los marcadores
            return render_template('resultado.html')

@app.route('/errores')
def busqueda_errores():
    return render_template('errores.html')

     
if __name__ == '__main__':
    app.run(debug=True,port=5017)