"""""
edad = input('Ingrese su edad: ')
edad = int(edad)
if edad > 18:
    print('Ud es mayor')
else:
    print('Ud no es mayor')

--------
EJ1

contraseña = "gonzalo"
pas = input('Ingrese contraseña ')

if contraseña == pas:
    print('Bienvenido!')  
        
else:
    print('Contraseña incorrecta, por favor reintente ')

-----------

EJ2
numero = int(input('Ingrese un numero: '))
if numero % 2 == 0:
    print('Su numero es par')
else:
    print('Su numero es impar')

EJ3
numero = int(input('Ingrese un numero: '))
for i in range (0, numero+1 ,2): ----------------> cuando usamos un range de 3 argumentos sabemos que el primer argumento es donde inicia la cuenta
            star   stop      step                           el 2do argumento es donde nesecitamos que se detenga
                                                   el 3er argumento es el incrementador, de cuanto en cuanto queremos que avance el mismo
    print(i,end=",")

EJ4
n = int(input('Ingrese su numero, por favor: '))
for i in range(n,-1,-1):
    print(i,end=',')


EJ5

inve=int(input('Cuanto dinero desea invertir: '))
años=int(input('Ingrese la cantida de años de su inversion: '))
interes=float(input('Ingrese la cantidad de interes anual: '))

for i in range(años):
   inve *= 1 + interes / 100
   interes_anual = inve
   print('Capital despues del ',str(i+1), ' años: ' ,round(interes_anual))

#other way

for i in range(1,años+1):
   inve *= 1 + interes / 100
   interes_anual = inve
   print('Capital despues del ',i, ' años: ' ,round(interes_anual))

EJ6   

num = int(input('Introduzca un numero '))
for i in range(num):
    for j in range(i+1):    --------------------> vectores, lo que hace es iterar la cantidad de veces de I + 1 ya que el otro FOR
                                                  arranca desde 0
        print("*" ,end="")
    print("")
    
EJ7

for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")


num=int(input('Ingrese un numero: '))
for i in range(1,num+1,2):
    for j in range(i,0,-2): ----------------> pasamos por i el parametro agregado en +2 
                                              y en J lo que hacemos es: ir del numero "I" hasta "0" , restando de -2 (hacemos la cuenta inversa en el mismo for)
        print(j,end="\t")
    print("")

"""""




    