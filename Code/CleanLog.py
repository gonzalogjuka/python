from tkinter import Tk 
from tkinter.filedialog import askopenfilename, asksaveasfilename

Tk().withdraw() 
infile = askopenfilename()
outfile = asksaveasfilename()
error = asksaveasfilename()


clean_phrases = ["#####","<?xml","npreMemory.c{DEP}","npDrvPublEVT","npreFindClose","SendRecvTCPMsg","npreMsg.c{DEP}@2922","npreControlProcess.c{DEP}@149","npreOSItf.c{DEP}@796","npreOSItf.c{DEP}@254"]
db = ["ERROR","N E W "]

with open(infile, "r") as inf, open(outfile, "w") as outf, open(error,"w") as errores:

    # ver el menu de los ejercicios condicionales para hacer un mini menu con numero o sino usar el tkinter
    for line in inf:
        if not any(phrase in line for phrase in clean_phrases):         
            line = line.rstrip()
            outf.write(line + '\n')
        if any(phrase in line for phrase in db):
            line = line.rstrip()
            errores.write(line + '\n')
