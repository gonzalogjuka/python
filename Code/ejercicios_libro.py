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

puntaje = input('Introduzca puntuacion: ')

def calcula_calificacion(numeros):
    try:        
        puntaje = float(numeros)
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


x = calcula_calificacion(puntaje)

n=5
while n > 0:
    print(n)
    n = n-1
print('Despegue')

while True: -------------------> obtenemos inputs del usuario hasta que escribe fin y sale del bucle
    linea = input('>')
    if linea == 'fin':
        break
    print(linea)

print('Terminado')


while True: 
    linea = input('>')
    if linea [0] == '#': -------> cuando escribo algo con # no se imprime por que finaliza la iteracion y salta de nuevo al while omitiendo el resto de las sentencias
                                  iteracion = vuelta
        continue
    if linea == 'fin':
        break
    print(linea)

print('Terminado') 


amigos = ['facu','manu','gaty','mati']  -------> lista
for amigo in amigos: -----------------------> ejecuta una vez para cada amigo que este en la lista de amigos
    print('Feliz año nuevo' , amigo)

print('Termine')


contador = 0
for valor[variable de iteracion] in [3,41,12,9,74,15](Lista): ------> como no usamos valor lo unico que hace es controlar que el bucle sea ejecutado 
                                                                      por cada valor de la lista
    contador = contador + 1

print('numero de elementos: ' , contador)

ej 2 : en vez de usar un sumador podemos usar la variable de iteracion para controlar la cantiad de elementos recorridos en la lista

total=0
for valor in [3,41,12,9,74,15]:
    total = total + valor -------> variable de iteracion que suma el numero actual recorrido (3+41+12+9+74+15) = 154
print('Total: ' , total)

mayor=None
print('Antes: ' ,mayor)
for valor in [3,41,12,9,74,15]:
    if mayor is None or valor > mayor:  -----> en cada iteracion le damos el mayor numero posible a "mayor", siempre comparandolo con "valor"
        mayor = valor ----------> asignamos el mayor valor a MAYOR hasta ese momento
    print('Bucle: ' , valor , mayor)
print('Mayor: ' , mayor)

menor=None
print('Antes: ' ,menor)
for valor in [3,41,12,9,74,15]:
    if mayor is None or valor < menor:  -----> en cada iteracion le damos el menor numero posible a "menor", siempre comparandolo con "valor"
        menor = valor ----------> asignamos el menor valor a MENOR hasta ese momento
    print('Bucle: ' , valor , menor)
print('Menor: ' , menor)

def min(valores):  --------> funcion interna min, sin explicacion [min ya tiene incorporado el print]
    menor = None
    for valor in valores:
        if menor is None or valor < menor:
            menor = valor
    return menor


        total_numeros = 0 ----> (t)
        cantiad_numeros = 0 ---> ok (i)
        media_numeros = total_numeros / cantiad_numeros (m)

"""

i = 0
t = 0
x2 = 0

try:
    
    while True:
        x=input ('Introduzca un numero: ')
        if x == 'fin':
            break       

        for numeros in [x]:
            i = i + 1
            x2 = int(x)
            t = x2
            print(x) #cambiar
            
        
except:
            print('Entrada invalida')
        
                

print('Cantidad de numeros: ' , i)
print('Dato almacenado en la lista T: ' ,t)
                # usar el 'continue' para volver a la iteracion
                # usar el print para mostar todos los numeros
                # usar otra variable para sacar la media
                # solucionar como almacenar los numeros y mostrarlos    
            