from flask import Flask,render_template,Response
from ddbb import db
from tkinter.filedialog import askopenfilename, asksaveasfilename


bases = db()
app=Flask(__name__)

def asd():
            bases[0]
            bases[1] 
            infile = askopenfilename()         
            outfile = asksaveasfilename(defaultextension='.xml',initialfile = "archivo")
            with open(infile, "r") as inf, open(outfile, "w") as outf:
                for line in inf:
                    if not any(phrase in line for phrase in bases[0]): 
                        if any(phrase in line for phrase in bases[1]):       
                            f = line.split()  
                            del f [0:5]
                            delimited=' '
                            b = delimited.join(f)       
                            outf.write(b + '\n')

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/logs')
def busqueda_log():   
            return render_template('logs.html')

@app.route('/resultado')
def resultado():
                asd()
                return render_template('resultado.html')

@app.route('/errores')
def busqueda_errores():
    return render_template('errores.html')

     
if __name__ == '__main__':
    app.run(debug=True,port=5017)