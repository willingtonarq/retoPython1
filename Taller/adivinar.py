#Realice  un  algoritmo  que  permita  adivinar  un  número  preestablecido  entre  1  y  10, 
#dando al usuario tres intentos, e informando si adivino o fallo. (ciclos + condicionales)

#for 
""" numero_secreto = 7
adivino = False

for intento in range(3):
    numero = int(input("Adivina el número (entre 1 y 10): "))
    if numero == numero_secreto:
        adivino = True
        break
    else:
        print("Incorrecto. Intenta de nuevo.")

if adivino:
    print("¡Felicidades! Adivinaste el número.")
else:
    print("Lo siento, fallaste los 3 intentos. El número era", numero_secreto) """

    
#while
numero_secreto = 6
intentos = 0
adivino = False

while intentos < 3:
    numero = int(input("Adivina el número (entre 1 y 10): "))
    intentos += 1
    if numero == numero_secreto:
        adivino = True
        break
    else:
        print("Incorrecto. Intenta de nuevo.")

if adivino:
    print("¡Felicidades! Adivinaste el número.")
else:
    print("Lo siento, fallaste los 3 intentos. El número era", numero_secreto)

