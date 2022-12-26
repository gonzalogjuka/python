# hacer una app de estadistica para tinder
# 1- hacer una db
# 2- tratar de hacerlo escalable
# 3- hacer algun tipo de buscador
# 4- 

"""i = 0 

while True:
    if i < 100:
        i = i + 1           
    else:
        continue

    print (i)
    break

import os ----> para realizar acciones del OS
os.system('mkdir prueba')
os.remove('prueba') ---> no funciona

import random
for i in range (5): # la cantidad de numeros que se muestran
    print(random.randint(1,50)) # rango de numeros

import subprocess
output = subprocess.check_output('dir',shell=True)
print(output)

import subprocess
output = subprocess.check_output('cd',shell=True)
print(output)

import subprocess
output = subprocess.Popen('mkdir prueba1',shell=True) ---> mientras el shell este abierto podemos ejecutar operacion con comandos de linux o windows
print(output)

import os
os.system('del prueba.txt') ----> del es para archivos 

import os
os.system('rmdir prueba') ----> rmdir o rm es para directorios 

def para las funciiones declaradas
ej

string='hello'

def my_print(string):
    print(string)

ej2 

string1='fobal'
print(string1)
>>> fobal

my_print(string1) ----> como definimos la funcion def my_print y le indicamos que lo unico que haga es imprimir un string aca la invocamos 
pero le indicamos via parametro que imprima el resultado que nesecitemos

>>> fobal

ej3

def hello_world_printer(): ----> aca hacemos lo mismo creamos una nueva funcion, pero no le pasamos el parametro, lo unico que hace es imprimir lo que contiene
    print('hello world')

hello_world_printer
>>> hello world

else if = elif


import random -------------->>>> no importa el orden de lectura primero escribimos la funciona luego la ejecucion

def numero(number):
    if number ==1:
        return 'es 1'
    elif number == 2:
        return 'es 2'
    elif number == 3:
        return 'es 3'
    elif number == 4:
        return 'es 4'
    elif number == 5:
        return 'es 5'

numero_random= random.randint(1,5) 
elegir= numero(numero_random)
print(elegir)

variable local
def fun1():
    num = 30
    print(num)


fun1()
>>> 30

variable global
num = 40
print(num)
num = 40
fun1 = 30

ej2

def fun1():
    global number
    number= 30

si quiero cambiar el valor de la funcion

number=40
print(number)
>>> 40

si quiero volver a la funcion original

fun1()
printer(number)
>>> 30
 
def fun1():
    global number --> variable global
    number= 30


def fun2(number):
    number +=1

number = 30
print (number)
>>> 30

fun2(number) ----> siempre el valor por defecto de number va a ser 30 segun lo declarado
print(number)
>>> 30

def fun2 (number)
number += 1
return(number) ----> para reflejar el resultado de la funcion tenemos que devolverlo con return

number = fun2 (number) ----> aca aplicamos el numero de la variable global (30) y lo aplicamos a la funcion pasandoselo como parametro
                             una vez ejecutada la funciona pasa el numero y lo suma, devolviendo el resultado del mismo
print(number)
>>> 31

"""