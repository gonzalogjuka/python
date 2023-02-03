from tkinter import Tk 
from tkinter.filedialog import askopenfilename, asksaveasfilename
# pyright: reportUnboundVariable=false
# ["#####","<?xml","npreMemory.c{DEP}","npDrvPublEVT","npreFindClose","SendRecvTCPMsg","npreMsg.c{DEP}@2922","npreControlProcess.c{DEP}@149","npreOSItf.c{DEP}@796","npreOSItf.c{DEP}@254"]
log = ["#####","<?xml","npreMemory.c{DEP}","npDrvPublEVT","npreFindClose","SendRecvTCPMsg","npreMsg.c{DEP}@2922","npreControlProcess.c{DEP}@149","npreOSItf.c{DEP}@796","npreOSItf.c{DEP}@254"]
errors = ["ERROR","N E W "]

Tk().withdraw()
pregunta = input('Que accion queres tomar?: \n\t1- Resumir Log\n\t2- Busqueda de solo errores\n\t3- Salir\n')
if pregunta == '3':exit()
if pregunta == '1':
    infile = askopenfilename()
    outfile = asksaveasfilename()
    with open(infile, "r") as inf, open(outfile, "w") as outf:
        for line in inf:
            if not any(phrase in line for phrase in log):         
                f = line.split()
                del f [0:7]
                delimited=' '
                f = delimited.join(f)
                f = line.rstrip()
                outf.write(f + '\n')

elif pregunta == '2':
    infile = askopenfilename()
    error = asksaveasfilename()
    with open(infile, "r") as inf, open(error, "w")as errores:
        for line in inf:
            if any(phrase in line for phrase in errors):
                line = line.rstrip()
                f = line.split()
                del f [0:7]
                delimited=' '
                b = delimited.join(f)
                errores.write(b + '\n')
                

