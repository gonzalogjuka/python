from tkinter import Tk 
from tkinter.filedialog import askopenfilename, asksaveasfilename
# pyright: reportUnboundVariable=false

clean_phrases = ["#####","<?xml","npreMemory.c{DEP}","npDrvPublEVT","npreFindClose","SendRecvTCPMsg","npreMsg.c{DEP}@2922","npreControlProcess.c{DEP}@149","npreOSItf.c{DEP}@796","npreOSItf.c{DEP}@254"]
db = ["ERROR","N E W "]

Tk().withdraw()
pregunta = input('Que accion queres tomar?: \n\t1- Resumir Log\n\t2- Busqueda de solo errores\n\t3- Salir\n')
if pregunta == '3':exit()
if pregunta == '1':
    infile = askopenfilename()
    outfile = asksaveasfilename()
    with open(infile, "r") as inf, open(outfile, "w") as outf:
        for line in inf:
            if not any(phrase in line for phrase in clean_phrases):         
                line = line.rstrip()
                outf.write(line + '\n')
                #Aplicar la funcion de abajo para los demas log's
elif pregunta == '2':
    infile = askopenfilename()
    error = asksaveasfilename()
    with open(infile, "r") as inf, open(error, "w")as errores:
        for line in inf:
            if any(phrase in line for phrase in db):
                line = line.rstrip()
                f = line.split()
                del f [0:7]
                delimited=' '
                b = delimited.join(f)
                print(b[10:])
                errores.write(b + '\n')
                

