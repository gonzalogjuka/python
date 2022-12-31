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
calucu_yuan = yuan * 0.14 / 1
def calculo_yuan(calucu_yuan):
    print('su cotizacion de pesos chinos en dolares es de: ' + str(calucu_yuan))
    return calucu_yuan

#Calcular en tiempo real la conversion de monedas YEN
calucu_yen = yen * 0.007 / 1
def calculo_yen(calucu_yen):
    print('su cotizacion de pesos japoneses en dolares es de: ' + str(calucu_yen))
    return calucu_yen

#Calcular en tiempo real la conversion de monedas WON
calucu_won = won * 0.0079 / 1
def calculo_won(calucu_won):
    print('su cotizacion de pesos koreanos en dolares es de: ' + str(calucu_won))
    return calucu_won


calculo_yuan((calucu_yuan))
calculo_yen((calucu_yuan))
calculo_won((calucu_won))

"""
