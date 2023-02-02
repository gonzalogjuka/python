from tkinter import Tk 
from tkinter.filedialog import askopenfilename, asksaveasfilename
# pyright: reportUnboundVariable=false

pregunta = input('Que accion queres tomar?: \n\t1- Resumir Log\n\t2- Busqueda de solo errores\n')

Tk().withdraw() 
try:
    if pregunta == '1':
        infile = askopenfilename()
        outfile = asksaveasfilename()
    if pregunta == '2':
        error = asksaveasfilename()
        outfile = asksaveasfilename()
except:
    print('Por favor ingresar un valor correcto')


clean_phrases = ["#####","<?xml","npreMemory.c{DEP}","npDrvPublEVT","npreFindClose","SendRecvTCPMsg","npreMsg.c{DEP}@2922","npreControlProcess.c{DEP}@149","npreOSItf.c{DEP}@796","npreOSItf.c{DEP}@254"]
db = ["ERROR","N E W "]

with open(infile, "r") as inf, open(outfile, "w") as outf, open(error,"w") as errores:

    for line in inf:
        if not any(phrase in line for phrase in clean_phrases):         
            line = line.rstrip()
            outf.write(line + '\n')
            outf.close()
        if any(phrase in line for phrase in db):
            line = line.rstrip()
            errores.write(line + '\n')
            errores.close()