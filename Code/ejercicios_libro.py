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

dato='From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'
arrobapos= dato.find('@')
print(arrobapos) ---- 21

espos= dato.find('',arrobapos)
print(espos) ---------- 31

direccion = dato[arroba+1:espos] ---------- el +1 es para que se muestre el caracter que le sigue al arroba
print(direccion)
utc.ac.za


camello=42
x='%d' % camello --------- %d es para pasar el formato a decimal
print(camello)

camellos=42
x='yo he visto %d camellos' % camellos
print(x)

x='En %d años he visto %g %s' % (3,0.1,'camellos')
print(x)

str='X-DSPAM-Confidence:0.8475'
cadena= str.find(':')
print('caracteres hasta el (:)',cadena) # 18
numero=str.find('5',cadena)
print('caracteres hasta el ultimo numero (5)',numero) # 24 (19 al 24 son numeros, para incluir el ultimo numero le tenemos que agregar un numero mas , del 0 al 18 son caracteres)
mostrar_n=str[19:25]
print(mostrar_n)
mostrar_p=str[0:cadena+1]
print(mostrar_p)

str.replace(old, new[, count])
Retorna una copia de la cadena con todas las ocurrencias de la cadena old sustituidas por new. Si se utiliza el parámetro count, solo se cambian las primeras count ocurrencias.

str.rfind(sub[, start[, end]])
Retorna el mayor índice dentro de la cadena s donde se puede encontrar la cadena sub, estando sub incluida en s[start:end]. Los parámetros opcionales start y end se interpretan igual que en las operaciones de segmentado. Retorna -1 si no se encuentra sub.
x=open('a.py') --------------> solo sirve si esta en el mismo directorio raiz
print(x)

x=open('a.py')
y = 0
for linea in x:
    y = y + 1 
print('contado de lineas: ',y)
print(x)

x=open('a.py')
lector = x.read() --------> si el archivo es chico podemos leerlo listando la longitud del mismo y printeandola con los arrays
print(len(lector))
print(lector[:52])

# Abrimos el fichero
fichero = open("a.txt", 'w')

# Tenemos unos datos que queremos guardar
lista = ["99710"]

# Guardamos la lista en el fichero
for linea in lista:
    fichero.write(linea + "\n")

# Cerramos el fichero
fichero.close()

x=open('pos28.xml')
print(x)
y = 0
for linea in x:
    if linea.startswith('1'):
        print(linea)

def buscar_dentro(nombre, texto):

    nro_linea = 0     
    with open(nombre) as archivo:
        for linea in archivo.readlines():
             nro_linea += 1
             if linea.find(texto) > - 1:
                break
        else:
            nro_linea = 0

    return nro_linea


    s = '1 2\t 3\n 4'
    print(repr(s))

    camellos=42
    'yo he visto %d de camellos' % camellos

from tkinter import Tk 
from tkinter.filedialog import askopenfilename, asksaveasfilename

Tk().withdraw() 
infile = askopenfilename()
outfile = asksaveasfilename()


with open(infile,"r") as archivo, open(outfile,"w") as outf:
    busqueda = input('Que buscas? ')
    for linea in archivo:
        if linea.find(busqueda) > -1: ----------------->  find busca una cadena dentro de otra y devuelva la posicion de la cadena
                                                          o (-1) si la cadena no fue encontrada
            print(linea)
            outf.write(linea)

lector = input('Introduzca el nombre del archivo: ')
archivo = open(lector,'r')
archivo2 = open('2.txt', 'w')
for linea in archivo:    ---------------> para recorrer un string podemos hacerlo sin algun condicional extra
    if linea:       
        archivo2.write(linea.upper())        


lector = input('Introduzca el nombre del archivo: ')
archivo= open(lector,'r')
archivo2= open('2.txt','w+')
stra='X-DSPAM-Confidence:'
spam_confidence=0
b = 0

for linea in archivo:
    if linea.find(stra) > -1:
       archivo2.write(linea)
       
archivo2 = open('2.txt','r+')

for linea in archivo2:
    a=linea[20:]
    b = b + 1
    a = float(a)
    spam_confidence = spam_confidence + a


promedio=spam_confidence / b
print('El promedio fue de: ',promedio)

lector = input('Introduzca el nombre del archivo: ')
contador=0

try:
    archivo= open(lector,'r')
    for linea in archivo:
        if linea:
            contador = contador + 1
    print('El texto tiene un total de: ' ,contador,' lineas')

except:
    print('Archivo inexistente')

numeros =[17,123]
numeros[1]= 5 --------> cuando el corchete esta adentro de la varible le indica cual es el valor dentro de esa ubicacion a cambiar
print(numeros)

quesos=['Cheddar','Edam','Gouda']
a ='Edam' in quesos
b = 'Gaviota' in quesos
print(a)
print(b)

numeros=[]
while True:
        valor=input('Ingrese un numero: ')
        if valor == 'fin':break
        a = int(valor)   
        numeros.append(a)      
        for i in range(len(numeros)):          
            numeros[i] = numeros[i]
           
print(numeros)

t = [1,2,304,4,5,50,1034]
t.sort() -----------------> ordena de memnor a mayor
print(t)

t=[1,2,3]
t2=[4,5,6]
t.extend(t2) --------> a la lista t le sumamos la lista t2 
print(t)

t = ['a','b','c']
eliminar = t.pop(1) ----> metodo para eliminar valor de la lista
del t[1] ---> lo elimina de una
t.remove('b') ------> si no sabes el indice del elemento, pero si sabes del dato , podes insertarlo
del t [0:3] ---> para remover todos los elementos dentro de ese rango, funciona lo mismo que los rebanados
print(t)
print(eliminar)

Funciones
nums=[1,2,3]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

num=list()
while(True):
    inp = input('Ingresa un numero: ')
    if inp =='fin' : break
    valor = float(inp)
    num.append(valor)
    for i in range(len(num)):          
            num = num         ---------> anteriormente en el otro ejercicio use la lista en formato [] generalmente se usa cuando sabes la informacion
                                         en este ejercicio usamos la lista 'Standar' que es () para cuando no sabemos la informacion y tenemos que tomar datos, podemos tener parametros como limites

print(num)

num=list()
while(True):
    inp = input('Ingresa un numero: ')
    if inp =='fin' : break
    valor = float(inp)
    num.append(valor)


promedio = sum(num) / len(num) --------> en la misma variable usamos la funcion suma y la funcion len para saber cuantos elementos tiene y cual es la suma de ellos
                                         con esta informacion en la misma variable podemos sacar un promedio facilmente sin tener que recurrir a otra variable para sumar la informacion
print(promedio)

s = 'hola'
t=list(s)
print(t) -----------> lista caracter por caracter

f = 'me gusta viciar'
a = f.split()
print(a)           --------------> lista palabra por palabra

'me gusta viciar'
'0   1     2'

print(a[2]) ------> podemos hacer con corchetes a la informacion que nesecitemos , la misma siempre se almacena en formato de lista

s = 'spamfspamfspamfspam'
delimitador = 'f'
res = s.split(delimitador) ------------> dentro de una palabra o lista .split puede tomar como parametros delimitadores
print(res)

t=['hola','yo','soy','goku']
delimitador = ' ' ---------> space
a = delimitador.join(t)
print(a)

x = open ('test.txt')
for linea in x:
    linea = linea.rstrip()
    if not linea.startswith('From '):continue
    a = linea.split() ---------> de esta manera todas las palabras que empiecen con XXX las podemos separar con split y una vez separadas dentro de una [] elegimos su ubicacion y las printeamos
    print(a[2])


x = open ('test.txt')
for linea in x:
    if not linea.startswith('From '):continue
    a = linea.split()
    print(a[2])    

a ='papa'
b ='papa'
a is b
#True ----> por que apuntan a lo mismo

a=['a','b','c']
b=['a','b','c']
a is b
#False ------> por que son dos objetos diferentes , dos listas (son equivalentes en informacion pero no identicas por que son diferentes objetos)

a = [1,2,3]
b = a ----> asociacion de variables se llama referencia
b is a
#True

b[0] = 17
print(a)
#[17,2,3] ----> al ser una referencia de muchos objetos, muta, es decir que los cambios que se efectuen en el mismo afectan a los demas que esten asociados
# en este ej, a B en el indice 0 le cambiamos el valor por 17

t1=[1,2]
t2 = t1.append(20) ----> lo que le pasas para agregar es consecutivo al indice que le sigue , solo informa el valor por parametro
print(t1)

t1=[1,2]
t3= t1 +  [3] --------> y el + crea una lista nueva
print(t3)
a = t1 is t3
print(a)


def recortar(x):
    del x[0:10]
    return None

def medio(x):
    return x[1:9]
    

nums=[1,2,3,4,5,6,7,8,10]
#a = recortar(nums) -----> hacemos una variable que llame la funcion recortar le pasamos por parametro nuestra lista que la misma es una alias del parametro X que esta en la funcion
#                          recorta la misma y devulve un NONE

#print(a)                  para printear el resultado llamos a la variable que llama a la funcion (PD= no podemos ejecutar otra funcion con los mismos datos en el orden 
#                          ya que toma el resultado de lectura de las funciones)

b = medio(nums)
print(b)

lector = open('test.txt','r')

lista = list()
for linea in lector:
    separador = linea.split()
    for linea in separador:           
        if linea not in lista[:]:
            lista.append(linea)               
            print(lista)
        else:
            print('Palabra repetida')
        
lista.sort()
print(lista)

lector = open('1.txt' , 'r')
b = list()
contador = 0
for linea in lector:
    x = linea.split()
    for linea in x:
        if linea.startswith('From'):
            contador= contador + 1
            if x[1] not in b[:]:     
                b.append(x[1])
b.sort()
print(b,"\nHay ",contador," lineas en el archivo con la palabra From")

b = list()
while True:
    a = input('Ingrese un numero: ')
    if a == 'hecho' :break
    parse = int(a)
    for i in a:
        if a not in b[:]:
            b.append(a)
            print(b)

print('Minimo: ',min(b))
print('Maximo: ',max(b))

#eng2sp = dict ()  # palabra reservada para diccionario
#eng2sp['one'] = 'uno'  # el primer valor one es el indice ahora llamado clave y el 'uno' es el valor de esa clave 
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'} # el orden del print pueden salir desordenados, pero para buscar un valor puntal nos regimos por la clave
#print(len(eng2sp))
#print(eng2sp['two'])
a ='one' in eng2sp # nos indica si la clave que le indicamos se encuentra en el diccionario
print(a)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
x=list(eng2sp.values()) # imprime los valores en forma de lista del diccionario
print(x)

palabra = 'cacona'
d = dict()
for linea in palabra:
    if linea not in d: # lo que hace con una palabra es que recorre letra por letra y la asigna en el for, si ya esta asignada lo suma a valor
        d[linea] = 1
    else:
        d[linea] = d[linea]+1

print(d)

palabra = 'cacona'
d = dict()
for i in palabra:
    d[i] = d.get(i,0) + 1 # el metodo get reemplaza al if else, por que si la clave aparece regresa el valor de la misma (si esta declarado)
                          # en este caso la palabra es cacona por ende si la informacion de I esta devuelve el valor correspondiente, sino suma +1
                          # pero si la calve no esta regresa el valor por defecto
print(d)

quest = input('Ingrese nombre del archivo: ')
try:
    lector=open(quest)
except:
    print('El archivo no se puede abrir ' ,quest)
    exit()

dic = dict()
for line in lector:
    divisor = line.split()
    for x in divisor:
        if x not in dic:
            dic[x] = 1   # lo que hacemos aca es parsear la palabra en linea, la dividimos por palabras
                         # para luego iterar palabra por palabra, si no esta darle un valor de 1
                         # y si esta sumarle +1 a esa frase
        else:
            dic[x] += 1

print(dic)

contador = {'chuck':1,'annie':42,'jan':100}
for clave in contador:   # el for recorre claves, no valores
    if contador[clave] > 10:
        print(clave,contador[clave])

contadores={'chuck':1,'annie':42,'jan':100}
lst = list(contadores.keys())
print(lst)
lst.sort()
for clave in lst:
    print(clave,contadores[clave])

import string
name = input('Ingrese el nombre del archivo: ')
try:
    lector = open(name)
except:
    print('El archivo no se encuentra disponible ',name)
    exit()

dic = dict()
for line in lector:
    line = line.rstrip() # quitamos salto de linea
    line = line.translate(line.maketrans('','',string.punctuation)) # quitamos signos de puntuacion
    line = line.lower() # quitamos mayuscualas
    separador = line.split() # separamos la frase en palabras
    for palabra in separador:
        if palabra not in dic:
            dic[palabra] = 1
        else:
            dic[palabra] += 1

print(dic)

import string

lector = open('1.txt','r')
dicio= dict()
for line in lector:
    line = line.rstrip() # quitamos salto de linea
    line = line.translate(line.maketrans('','',string.punctuation)) # quitamos signos de puntuacion
    line = line.lower() # quitamos mayuscualas
    divi = line.split() # separamos la frase en palabras
    for x in divi:
        dicio[x] = dicio.get(x,0) + 1 # esto remplaza al if,else y al not in 
                                      # si la clave se encuentra en el diccionario , GET regresa
                                      # el valor que contiene en el diccionario
                                      # sino devuelve el valor por defecto "0"
  

print(dicio)

lector = open('1.txt','r')
diccio = dict()
for line in lector:  
    if line.startswith('From'):
        a = line.split()
        del a [0:2]
        del a [1:]
        for palabra in a:       
            if palabra not in diccio:
                diccio[palabra] = 1
            else:
                diccio[palabra] += 1

print(diccio)

lector = open('1.txt','r')
diccio = dict()
for line in lector:
    if line.startswith('From'):
        a = line.split()
        del a [0]
        del a [1:]
        for palabra in a:       
            if palabra not in diccio:
                diccio[palabra] = 1
            else:
                diccio[palabra] += 1

print(diccio)

lector = open('1.txt','r')
diccio = dict()
for line in lector:
    if line.startswith('From'):
        a = line.split()
        del a [0]
        del a [1:]
        for palabra in a:       
            if palabra not in diccio:
                diccio[palabra] = 1
            else:
                diccio[palabra] += 1               

lst = list(diccio.keys()) # una manera mas comoda de lectura es armar una lista y pasar todo el contenido del diccionario
                          # para luego orderlarlo y con un for recorrerlo
                          # el metodo keys obtiene las claves de un diccionario (es decir el valor que se le introduce)
                          # el diccionario guarda la clave (indice) y el valor del indice 
lst.sort()
for clave in lst:
    print(clave,diccio[clave])


lector = open('1.txt','r')
diccio = dict()
for line in lector:
    if line.startswith('From'):
        a = line.split()
        del a [0]
        del a [1:]
        for palabra in a:       
            if palabra not in diccio:
                diccio[palabra] = 1
            else:
                diccio[palabra] += 1               

lst = list(diccio.keys()) 
lst.sort()
for clave in lst:
    print(clave,diccio[clave])

 
mayor=0
menor=0
for clave in diccio:
    f = int(diccio[clave])
    contador = f
    if mayor is 0 or contador > mayor:
        mayor = contador
        
    elif menor is 0 or contador < menor:
        menor = contador
    
    

print('Minimo: ',mayor)
print('Maximo: ',menor)

lector = open('1.txt','r')
diccio = dict()
for line in lector:
    if line.startswith('From'):
        a = line.split()
        del a [0]
        del a [1:]
        for palabra in a:
            palabra[-10:] # lo que hacemos es acceder al string bajo corchetes y con el '-' eliminamos los caracteres que nesecitemos
                          # en pocas palabras, recortamos un string y lo pasamos
            if palabra not in diccio:
                diccio[palabra] = 1
            else:
                diccio[palabra] += 1               

lst = list(diccio.keys()) 
lst.sort()
for clave in lst:
    print(clave,diccio[clave])

lector = open('1.txt','r')
diccio = dict()
for line in lector:
    if line.startswith('From'):
        a = line.split()
        del a [0]
        del a [1:]
        for palabra in a:
            palabra=palabra[-10:] # lo que hacemos es acceder al string bajo corchetes y con el '-' eliminamos los caracteres que nesecitemos
                                  # en pocas palabras, recortamos un string y lo pasamos
            if palabra not in diccio:
                diccio[palabra] = 1
            else:
                diccio[palabra] += 1               

lst = list(diccio.keys()) 
lst.sort()
for clave in lst:
    print(clave,diccio[clave])

lector = open('1.txt','r')
diccio = dict()
for line in lector:
    if line.startswith('From'):
        a = line.split()
        del a [0]
        del a [1:]
        for palabra in a:
            domain = palabra.split('@')[1] # la mejor manera de hacerlo es un split en el caracter que nesecitemos
                                            # y el [-1/1] es para acceder al ultimo caracter de la lista, osea si filtramos por @ es el que le sigue ya que el 0 es el primero
                                            # ej: stephen.mackrut @ uct.ac.za
            if domain not in diccio:        #            0             1
                diccio[domain] = 1
            else:
                diccio[domain] += 1               

lst = list(diccio.keys()) 
lst.sort()
for clave in lst:
    print(clave,diccio[clave])

x = ('a','b','c','d') #pueden ir sin los parentesis
t = ('a',) # la tupla de un solo elemento va con la , al final-. Si se la sacamos python la toma como un str
f = tuple()
t = tuple('piripitiflautico') # si el argumento es una cadena, lista o tupla. El resultado es una tupla con los elementos en secuencia
print(t) #('p', 'i', 'r', 'i', 'p', 'i', 't', 'i', 'f', 'l', 'a', 'u', 't', 'i', 'c', 'o')
print(x[0]) # 'a' , el operador corchete indexa un elemento de la tupla
print(x[1:3]) # 'b' y 'c' - a es el 0 , b el 1 , c el 2 y ya el ultimo elemento no lo muestra
              # tambien funciona como rebanador
# la informacion de la tupla no se puede modificar , pero si se puede reemplazar una tupla por otra
x = ('A',) + x[1:]
print(x)

# se puede comparar tuplas
a = (2, 4, 6, 8)
b = (3, 4, 7, 9)
a = (0, 1, 2) < (0, 3, 4) # lo ejecuta correctamente
print(a)

#print ("A is greater than B:", a > b) # a pesar del error lo ejecuta igual


#a = sorted([15, 2, 33]) # lo ordena por asendencia, solo funciona en lista
#a =[(15, 2, 33)] # tupla
a.sort()
print(a)
Omitir el .sort()

txt = 'Pero que luz se deja ver alli'
palabras = txt.split()
t = list()
for palabra in palabras:
    t.append((len(palabra),palabra)) # genera la tupla donde cada palabra es precedida por su longitud

t.sort(reverse=True) # reserve true indica orden decreciente
res = list()
for longitud,palabra  in t: # cuando tenemos una tupla con algun digito precedido, en el for tenemos
                            # tenemos que utilizar 2 argumentos tal cual como cuando lo agregamos
                            # el primero sera el digito/valor y el segundo sera la clave
    res.append(palabra)

print(res)

m = ['pasalo','bien']
x,y = m # una secuencia la asignamos a 2 variables, estas tambien puede representarse asi
        # (x,y) = m
print(x)
print(y)

# esto se traduce asi, python asigna aproximadamente la sintaxis de asignacion tupla

m = ['pasalo','bien']
x = m[0]
y = m[1]

print(x)
print(y)


# para intercambiar tuplas podemos asignar los valores asi
# tupla variable      # tupla de expresiones  
a,b              =    b,a 

a,b = 1,2,3 #wrong, tiene que ser iguales en cantidad de informacion

dir = 'monty@python.com'
nombre,dominio = dir.split('@') # crea 2 listas y le pasa como informacion 1 valor a cada una , una antes de split y otra despues
print (nombre)
print (dominio)


d = {'a':10,'b':1,'c':22}
t = list(d.items()) # enlistamos la infomacion de un diccionario por items
t.sort()
print(t)

d = {'a':10,'b':1,'c':22}
for clave,valor in list(d.items()): #1ª parametro string , 2do int, ver print
    print(valor,clave) # esto se imprime por valor almacenado

d = {'a':10,'b':1,'c':22}
l = list()
for clave,valor in d.items():
    l.append((valor,clave))

print(l)
l.sort(reverse=True)
print(l)

t = list()
d = dict()
with open('1.txt', "r") as entrada, open('outfile.txt', "w") as salida:
    for i in entrada:
        if i.startswith('From:'):
            separador=i.split()
            del separador[0]
            for x in separador:
                if x not in d:
                    d[x] = 1
                else:
                    d[x] += 1

    for clave,valor in list(d.items()):
        t.append((valor,clave))
        t.sort(reverse=True) # si no le pasas por parametro el orden, lo ejecuta por orden de lectura y lo printea

print(t[:1]) # con este parametro mostramos los 10 mas grandes


filename = input('Nombre del archivo: ')
fhand = open(filename,'r')
d = dict()

for i in fhand:
    if i.startswith('From '):
        tiempo = i.split()[3] # por tupla pasamos el parametro a recortar en ves de parsear y deletear el resto
                              # adicionalmente nos trae la palabra en la ubicacion exacta
        hora = tiempo.split(':')[0]
        d[hora] = d.get(hora,0) + 1 # el .get busca en el diccionario y en esta ocacion le pasamos 2 parametros
                                    # en primer parametro le pasmos la varialbe hora y si la misma es de valor 0 se le suma +1
                                    # de esta manera se realiza un contador de datos para las lineas leidas

                                    
                    t = list(d.items()) #en ves de iterar la lista para obtener los .items()
                    # se lo podemos pasar como parametro directamente
t.sort()
for x in t:
    print(x[0],x[1]) #podemos valor la clave valor con las ubicaciones de la lista
#for clave,valor in d.items():
 #   t.append((clave,valor))
  #  t.sort(reverse=True)
"""
import re
x = open('1.txt')
for line in x:
    line = line.rstrip()
    f= re.findall(r'^From .* ([0-9][0-9]):([0-9][0-9])',line)
    if len(f) > 0:
        print(f[0][0]+':'+f[0][1]) # si tenemos 2 valores en el mismo indice usamos los sub indices como acontinuacion para unirlos o concatenarlos
                # indice       #subindice       ok  






     
