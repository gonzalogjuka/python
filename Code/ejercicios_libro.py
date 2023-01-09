ent = input ('Introduzca temperatura')
try:
    fahr = float(ent)
    cel = (fahr - 32.0) * 5.0 / 9.0
    redondeo = round (cel)
    print (redondeo)
except: 
    print('Ingrese un numero, por favor ')
