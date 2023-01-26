from tkinter import Tk 
from tkinter.filedialog import askopenfilename, asksaveasfilename

Tk().withdraw() 
infile = askopenfilename()
outfile = asksaveasfilename()

clean_phrases = ["DEBUG","#####","<?xml","npreMemory.c{DEP}","npDrvPublEVT","npreFindClose","SendRecvTCPMsg"]

with open(infile, "r") as inf, open(outfile, "w") as outf:

    for line in inf:
        if not any(phrase in line for phrase in clean_phrases):
            outf.write(line)
