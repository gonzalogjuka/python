"""
EJ1

edad=int(input('Introduzca su edad: '))
if edad > 18:
    print('ud es mayor!')
else:
    print('ud es menor')

EJ2

key="gonzalo"

login=input("Por favor,ingresar la contraseña: ")
if key == login:
    print('Binvenido!')
else:
    print('Contraseña incorrecta')

EJ3

n1=int(input('Por favor,ingresa un numero: '))
n2=int(input('Por favor,ingresa otro numero mas: '))

if n2 == 0:
    print('Eligio como el hoyo')
else:
    print(n1/n2)

EJ4

n1=int(input('Ingrese un numero: '))
if n1 % 2 == 0:
    print('Su numero es par!')
else:
    print('Su numero es impar')

EJ5

edad=int(input('Ingrese su edad: '))
ingresos=int(input('Coloque sus ingresos: '))

if edad > 16 and ingresos >= 1000:
    print('Usted debe tributar!')
else:
    print('No debe tributar')

EJ6
nombre=input('Ingrese su nombre: ')
sexo=input('Indique su sexo: M o H ')

if nombre > "n" or "m" and sexo == "H" or "M" :
    print('Usted pertenece al grupo A')
else:
    print('Usted pertenece al grupo B')

EJ7
renta=int(input('Indique su enta anual: '))
if renta < 10000:
    print('5%')
elif renta < 20000:
    print('15%')
elif renta < 35000:
    print('20%')
elif renta < 60000:
    print('30%')
else:
    print('45%')

EJ8
puntaje=float(input('Introduza el puntaje: '))
dinero=2400
if puntaje < 0.0:
    bonus = dinero * puntaje
    print('Nivel Inaceptable, con una mejora salarial de: ' ,bonus)
elif puntaje < 0.4:
    bonus = dinero * puntaje
    print('Nivel Aceptable, con una mejora salarial de:' ,bonus)
else: 
    bonus = dinero * puntaje
    print('Puntaje Meritorio, con una mejora salarial de: ' ,bonus)

EJ9
edad=int(input('Cual es su edad: '))
if edad < 4:
    print('Puede pasar gratis!')
elif edad <= 18:
    print('Debe pagar 5$')
else:
    print('Debe pagar 10$')

EJ10
pizza=input('Que tipo de pizza va a elegir: \nTipos de pizza:\n\t1- Vegetariana\n\t2- No vegetariana\n ')
if pizza == '1':
    ingrediente_vege=input('Eliga un ingrediente para su pizza: \n\t1- Pimiento \n\t2- Tofu\n ')
    if ingrediente_vege == '1':
        print('Usted ordeno una pizza vegetariana con pimiento')
    else:
        print('Usted ordeno una pizza vegetariana con tofu')


if pizza == '2':
    ingrediente_novegie=input('Eliga un ingrediente para su pizza: \n\t1- Peperoni \n\t2- Jamon \n\t3- Salmon\n ')
    if ingrediente_novegie == '1':
        print('Usted ordeno una pizza con peperoni')
    elif ingrediente_novegie == '2':
        print('Usted ordeno una pizza con jamon')
    else:
        print('Usted ordeno una pizza con salmon')
"""


