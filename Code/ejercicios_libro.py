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

i = 0
t = 0

while True:
        x=input ('Introduzca un numero: ')
        if x == 'fin':
            break
        try:
            x2 = float(x)
        except:
            print('Numero Incorrecto')
            continue       

        i = i + 1 -----> hacemos una varible que cuente la cantidad de inputs generados, siendo que la misma inicia en cero , sumamos su valor mas + 1 de iteracion
        t = t + x2 ----> hacemos una variable que cuente el total de los numeros, siendo la misma en 0 + los numeros ingresados parseados a INT


print('Cantidad de numeros: ' , i)
print('Total: ' ,t)
print('La media es: ' ,t/i)


mayor = None
menor = None

while True:
    x =input("Ingrese un numero: ")
    if x == 'fin':break
    x2 = int(x)
    try:
        if mayor is None or x2 > mayor:
            mayor = x2
            print(mayor)
        elif menor is None or x2 < menor:
            menor = x2
            print(menor)

    except:
        print('valor invalido')
        continue


print('El numero maximo es: ' ,mayor)
print('El numero minimo es: ' ,menor)



fruta = 'banana'
letra = fruta[1] ----> imprime la letra del espacio 1
b[0]a[1]n[2]a[3]n[4]a[5]
print(letra)

fruta = 'banana'
a= len(fruta) --------> nos indica la cantidad de carecteres en cadena
print(a)

fruta='banana'
tamaño= len(fruta)
ultima= fruta[tamaño-1] = devuelve la ultima letra de la frase ya que len cuenta 6 letras y empieza del 1 y no del 0
                          por ende al LEN le restamos 1 para imprimir la ultima letra
print (ultima)

fruta='banana'
indice = 0 
while indice < len(fruta):
    letra = fruta[indice]
    print(letra)
    indice = indice + 1

fruta='banana'
indice = 5
leng = 6
while indice < leng:
    letra = fruta[indice]
    print(letra)
    leng = leng - 1
    indice = indice - 1
    if indice == -1:
        break
        
fruta = 'banana'
print(fruta[:]) ---------> imprime todo de principio a final

def cuenta(a,b):
    contador = 0
    for b in a:
        if b == 'a':
            contador = contador + 1
    return contador

print(cuenta('banana','a'))

#ejemplo in
#'a' in 'banana'
#True
#'semilla' in 'banana'
#False


palabra = 'banana'
if palabra == 'banana':
    print('muy bien bananas')

palabra = 'Anana'       ------------------> para ordenar alfabeticamente tambien sirven la comparacion, menor, mayor, ect..
if  palabra < 'banana' :   
    print('tu palabra ' + palabra + ' esta antes que banana')
else:
    print('tu palabra ' + palabra + ' esta antes que despues')

palabra = 'banana'
nueva_palabra = palabra.upper() ----------- metodo para pasar todo a mayus
print(nueva_palabra)

palabra = 'banana'
indice = palabra.find('a') -----------  metodo para buscar una letra dentro de la cadena expuesta
print(indice)

palabra = 'banana'
indice = palabra.find('na',3) ----- tambien puede tomar como 2do parametro la ubicacion de donde empezar a buscar la cadena prevista
print(indice)


palabra = '  Aqui vamos   '
nueva=palabra.strip() --------------------- para borrar los espacios en blanco o tabs , del princio o final de una oracion
print(nueva)

palabra = 'Aqui vamos'
nueva=palabra.startswith('aqui')  --------------------- devuelve un bool si la la cadena se encuentra en la provista antes del metodo
                                                        este mismo metodo requiere de mayus y minus
print(nueva)
x=palabra.startswith('F')
print(x)


palabra = 'Que tengas un buen dia'
nueva=palabra.startswith('q')
print(nueva)
x=palabra.lower()   ------------------------- para pasarla a minus, usamos lower, vemos que al principio por estar en minus no reconoce el bool
                                              parseamos la palabra a minus y lanzamos el doble parametro dentro de la misma linea y asi lo reconoce
print(x)
x=palabra.lower().startswith('q')
print(x)


palabra = 'banana'
buscador=palabra.count('a'[0:5])
print(buscador)

camello=42
x='%d' % camello --------- %d es para pasar el formato a decimal
print(camello)

camellos=42
x='yo he visto %d camellos' % camellos
print(x)

x='En %d años he visto %g %s' % (3,0.1,'camellos')
print(x)

"""
