import random  
# pyright: reportUnboundVariable=false
# respetar las tabulaciones, 1 tabulacion para cada variable: ej: auto (1 tab) , print (1 tab debajo de auto)

def adivina_numero():
    global guest   
    for i in range(0,4):
        print('Intenta adivinarlo')
        guest= int(input('Ingresa un numero del 1 al 20: '))

        if guest < secretNumber:
            print('El numero es muy bajo')
        elif guest > secretNumber:
            print('El numero es muy alto')                   
        else:
            break
   # return guest

def chequeo(guest,secretNumber):
    if guest == secretNumber:
        print('Felicidades el numero es el correcto')  
    else: 
        print('Segui participando, el numero era: ' , secretNumber)

secretNumber = random.randint(1,20)
print('Estoy pensando un numero')

# guest = adivina_numero() --> otra forma de resolverlo es retornado el resultado y asignandoselo a la funcion
adivina_numero()
chequeo(guest,secretNumber)