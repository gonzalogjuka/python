import random  
# pyright: reportUnboundVariable=false

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

secretNumber = random.randint(1,20)
print('Estoy pensando un numero')

adivina_numero()

if guest == secretNumber: # type: ignore
    print('Felicidades el numero es el correcto')  
else: 
    print('Segui participando, el numero era: ' + str(secretNumber))
