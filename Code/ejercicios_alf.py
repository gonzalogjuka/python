"""""
edad = input('Ingrese su edad: ')
edad = int(edad)
if edad > 18:
    print('Ud es mayor')
else:
    print('Ud no es mayor')

--------


contraseña = "gonzalo"
pas = input('Ingrese contraseña ')

if contraseña == pas:
    print('Bienvenido!')  
        
else:
    print('Contraseña incorrecta, por favor reintente ')

-----------

numero = int(input('Ingrese un numero: '))
if numero % 2 == 0:
    print('Su numero es par')
else:
    print('Su numero es impar')

numero = int(input('Ingrese un numero: '))
for i in range (0, numero+1 ,2): ----------------> cuando usamos un range de 3 argumentos sabemos que el primer argumento es donde inicia la cuenta
            star   stop      step                           el 2do argumento es donde nesecitamos que se detenga
                                                   el 3er argumento es el incrementador, de cuanto en cuanto queremos que avance el mismo
    print(i,end=",")

n = int(input('Ingrese su numero, por favor: '))
for i in range(n,-1,-1):
    print(i,end=',')

"""""


