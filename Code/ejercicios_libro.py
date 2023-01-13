""""
ent = input ('Introduzca temperatura')
try:
    fahr = float(ent)
    cel = (fahr - 32.0) * 5.0 / 9.0
    redondeo = round (cel)
    print (redondeo)
except: 
    print('Ingrese un numero, por favor ')


horas= input('Introduzca horas ')
tarifa= input('Introduzca tarifa ') ----> hacemos inputs generales para cualquier informacion
try:
    horas = int(horas)  ----------> si usamos try and except, podemos convertir dicha informacion previo a los parametros que vamos a indicar, tambien podemos indicarselo afuera del if y convertir al tipo de dato
                                    que nesecitemos manipular
    tarifa = int (tarifa)
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
except:
        print('Error,por favor coloque un valor numerico.')


EJ2:

horas = input('Introduzca horas ')
tarifa = input('Introduzca tarifa ')
horas = int(horas)
tarifa = int(tarifa)

if horas > 40:
        horas_extras = horas - 40
        tarifa_extra = tarifa * 1.5
        calculo_extras = horas_extras * tarifa_extra
        salario = tarifa * 40
        nuevo_salario = salario + calculo_extras
        print(nuevo_salario)
else:
    salario_normal = horas * tarifa
    salario_str = str(salario_normal)
    print('Me gustan los billetes')
    print('Y no olvides que tu salario es de: $' + salario_str + ' pesos puerco espin')


puntaje = input('Introduzca puntuacion: ') -------> recordar siempre hacer un input sin tipo de variable y la misma meterla adentro de los condicionales para que recorra las funciones
                                                    sino intentara convertir el tipo de dato que introduzcamos a el tipo de dato que le indiquemos

try:
    puntaje = float(puntaje)
    if puntaje >= 0.9:
        print('Sobresaliente')
    elif puntaje >= 0.8:
        print('Notable')
    elif puntaje >= 0.7:
        print('Bien')
    elif puntaje >= 0.6:
        print('Suficiente')
    else:
        print('Insufuciente')
except:
    print('Puntuacion Incorrecta.')

def consulta():
    print ('Hola soy el print de la primera funcion')

def consulta_al_cuadrado():
    consulta()
    print('Hola estoy llamando a una funcion dentro de otra')


print(consulta)
print(type(consulta))
consulta_al_cuadrado()

import random

for i in range(10):
    x = random.random()
    print(x)

import random

number = random.randint(5,10)
print(number)


def estribillo():
    print('parte 1')
    print('parte 2')

repite() ---------------------> para llamar a la funcion primero debe crease, por ende la ejecucion tiene que estar despues que la propia llamada a la misma

def repite():
    estribillo()
    estribillo()

repite() --------------> este es el lugar correcto de ejecucion



def repite():
    estribillo()
    estribillo()

def estribillo():
    print('parte 1')
    print('parte 2') ----------------> a pesar de que se cambio el orden de las definiciones funciona correctamente cuando hacemos la llamda indirecta o directamente

repite()

michael= 'aguante el gta'
def llamada(bruce):            -------> esta funcion le asignamos un parametro que se lo pasamos a los print
                                        cuando hacemos la llamada podemos pasar el parametro o la indicacion que nesecitemos
                                        tambien, como se muestra el ejemplo podemos crear variables y pasarselas para que las tome como paremetro de nuestra funcion
    print(bruce)
    print(bruce)

llamada(michael)

import math

a = math.sqrt(25) ----> raiz cuadrada
print(a)

def sumados(a,b):
    suma = a + b
    return suma ------> devulve la informacion a la funcion

x = sumados(3,5)
print(x)

def[definicion de funcion] sumados[funcion](a,b[parametros]): 
    suma[variable local] = a + b
    return[resultado de funcion] suma ---> al aplicar return le estamos pasado como resultado de la funcion , la variable local "suma" declarada previamente

if(sumados(1,80[argumentos]) > 20):
    print('cosas locas')
else:
    x = sumados(3,5)
    print(x)


RECORDAR: ---> cuando llamamos a una funcion saltea la ejecuccion y cuando termina vuelve desde donde se quedo
               siempre se crea la funcion y luego la ejecuccion

horas = input('Introduzca horas: ')
tarifa = input('Introduzca tarifa: ')
horas = int(horas)
tarifa = int(tarifa)

def calculo_salario(horas,tarifa):
    if  horas > 40:
        horas_extras = horas - 40
        tarifa_extra = tarifa * 1.5
        calculo_extras = horas_extras * tarifa_extra
        salario = tarifa * 40
        nuevo_salario = salario + calculo_extras
        return nuevo_salario
    else:
        salario_normal = horas * tarifa
        return salario_normal

x = calculo_salario(horas,tarifa) ---> pedimos datos por input, parseamos los datos a int y luego llamamos a la funcion "calculo_salarial"
                                       asignado una variable cualquiera para pasarle la informacion del input como argumentos de la funcion, hacia los parametros de la misma
                                       tomando los datos numericos y ejecutandolos para devolver el resultado por return
print (x)
"""




