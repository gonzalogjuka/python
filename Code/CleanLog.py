from tkinter import Tk 
from tkinter.filedialog import askopenfilename, asksaveasfilename
# pyright: reportUnboundVariable=false

clean_phrases = ["DEBUG"]
db = ["ERROR","N E W "]

Tk().withdraw()
pregunta = input('Que accion queres tomar?: \n\t1- Resumir Log\n\t2- Busqueda de solo errores\n\t3- Salir\n')
if pregunta == '3':exit()
if pregunta == '1':
    infile = askopenfilename()
    outfile = asksaveasfilename()
    with open(infile, "r") as inf, open(outfile, "w") as outf:
        for line in inf:
            if any(phrase in line for phrase in clean_phrases):         
                line = line.rstrip()
                outf.write(line + '\n')
elif pregunta == '2':
    infile = askopenfilename()
    error = asksaveasfilename()
    with open(infile, "r") as inf, open(error, "w")as errores:
        for line in inf:
            if any(phrase in line for phrase in db):
                line = line.rstrip()
                errores.write(line + '\n')
                

