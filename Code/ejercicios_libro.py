""""
ent = input ('Introduzca temperatura')
try:
    fahr = float(ent)
    cel = (fahr - 32.0) * 5.0 / 9.0
    redondeo = round (cel)
    print (redondeo)
except: 
    print('Ingrese un numero, por favor ')
"""

horas= int (input('introduzca horas'))
tarifa= int (input('introduzca tarifa'))


if horas > 40:
    horas_extras = horas - 40
    tarifa_extra = tarifa * 1.5
    calculo_extras = horas_extras * tarifa_extra
    salario = tarifa * 40
    nuevo_salario = salario + calculo_extras
    print(nuevo_salario)
else:
    salario_normal= horas * tarifa
    print(salario_normal)
    

     

