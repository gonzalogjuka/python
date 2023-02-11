from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return 'Desarrollada por Gonzalo Gjuka - gonzalo.gjuka@hotmail.com'

if __name__ == '__main__':
    app.run(debug=True,port=5017)