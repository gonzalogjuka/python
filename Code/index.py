from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/logs')
def busqueda_log():
    return render_template('logs.html')

@app.route('/errores')
def busqueda_errores():
    return render_template('errores.html')

if __name__ == '__main__':
    app.run(debug=True,port=5017)