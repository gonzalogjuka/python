""" It's is a test for github, another incomming commit
celcius = 20
fahrenheit = 40

celcius = (fahrenheit - 32) /18
print(celcius)

mass = 80
height = 1.77

bmi = mass/height ** 2
print(bmi)

# Quadratic Formula 🧮
# Codédex , para calcular la raiz de un numero es lo mismo que poner **0.5 

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

root1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
root2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)

print(root1)
print(root2)

 
yuan = int(input('cuanto tenes en yuan '))
yen = int(input('cuanto tenes en yen '))
won = int(input('cuanto tenes en won '))

#Calcular en tiempo real la conversion de monedas YUAN
calucu_yuan = yuan * 0.14
def calculo_yuan(calucu_yuan):
    print('su cotizacion de pesos chinos en dolares es de: ' + str(calucu_yuan))
    return calucu_yuan

#Calcular en tiempo real la conversion de monedas YEN
calucu_yen = yen * 0.007
def calculo_yen(calucu_yen):
    print('su cotizacion de pesos japoneses en dolares es de: ' + str(calucu_yen))
    return calucu_yen

#Calcular en tiempo real la conversion de monedas WON
calucu_won = won * 0.0079
def calculo_won(calucu_won):
    print('su cotizacion de pesos koreanos en dolares es de: ' + str(calucu_won))
    return calucu_won


calculo_yuan((calucu_yuan))
calculo_yen((calucu_yuan))
calculo_won((calucu_won))

import random

grade = random.randint(0,100)

if grade > 50:
    print('aprovaste puerca')
else:
    print('desaprovaste gorda')


ph = int(input('Ingrese valor de ph de la sustancia '))
if ph > 7:
    print('Basico')
elif ph < 7:
    print('Acido')
else:
    print('Natural')



import random

question = input('Question: ')
random_number = random.randint(1, 9)
# print(random_number)

if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer = 'Better not tell you now'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
else:
  answer = 'Error'
  
print('Question:' + question)
print('Magic 8 Ball:' + answer)



gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('Te gustan las serpientes o las aguilas')
print('1) Aguilas')
print('2) Serpientes')
Q1 = int(input('Eliga opcion: '))


if Q1 == 1:
    gryffindor =+ 1
    ravenclaw =+ 1
elif Q1 == 2:
    slytherin =+1
    hufflepuff =+1
else:
    print('elegi bien mogul')

print('Que infusion te gusta?')
print('1) Te')
print('2) Cafe')
print('3) Mate')
print('4) Matecocido')
Q2 = int(input('Eliga opcion: '))


if Q2 == 1:
        hufflepuff =+1
elif Q2 == 2:
        slytherin =+1       
elif Q2 == 3:
         ravenclaw =+1
elif Q2 == 4:
        gryffindor =+1
else:
    print('elegi bien picaron')
    


print('Que instrumento te gusta?')
print('1) Violin')
print('2) Guitarra')
print('3) Trompeta')
print('4) Bateria')
Q3 = int(input('Eliga opcion: '))


if Q2 == 1:       
        slytherin =+1   
elif Q2 == 2:
        hufflepuff =+1      
elif Q2 == 3:
         ravenclaw =+1
elif Q2 == 4:
        gryffindor =+1
else:
    print('elegi bien picaron')

if gryffindor >= slytherin and gryffindor >= ravenclaw and gryffindor >= hufflepuff:
    print('Sos un maricon')
elif slytherin >= ravenclaw and slytherin >= hufflepuff:
    print('Sos un crack')
elif ravenclaw >= hufflepuff:
    print('Sos un mascatuerca')
else:
    print('Sos un toro mecanino norteño de la puna')



print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

  if pin == 1234:
    print('PIN accepted!')

for i in range (100):
  print ("no debo usar snap en clase" )
  print(i)


for i in range (99,0,-1):  # el primer numero del parametro indica el inicio del conteo y el 2do numero es los numeros enteros menores a el y el 3er numero lo que indica es el incremento que se le da cada vez que itera
  como el parametro va de mayor a menor se le agrega el 3er parametro para que vaya restando ya que no podemos restar cero, por ende la ultima linea de codigo donde resta -1 entonces cuando el for itera hace
  -1 + -1 = 1 (1 y 2 parametro rangos desde donde queremos incluir los numeros y 3 parametro el incremental si es de mayor a menor resta y si es de menor a mayor suma)

  print(f'{i} bottles of beer on the wall') # el f' es un parametro para colocar la iteracion de STRING con {} , recordemos que lo que cuenta son strings y no INT , por ende nos va a dejar printearlo
  print(f'{i} bottles of beer')
  print('Take one down, pass it around')
  print(f'{i-1} bottles of beer on the wall')


for num in range(1,101):
  if num % 3 == 0 and num % 5 == 0: # 
    print('FizzBuzz')
  elif num % 3 == 0:
    print('Fizz')
  elif num % 5 == 0:
    print('Buzz')
  else:
    print(num)

    
for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
  elif num % 3 == 0:
    print('Fizz')
  elif num % 5 == 0:
    print('Buzz')
  else:
    print(num)

    for num in range(1,41):
  if num % 3 == 0: # numero multiplo , es el numero a multiplicar por los numeros naturales (1,2,3,4,5,6) como las tablas
    print (f'{num} Multiplo')
  else:
    print(num)

"""

