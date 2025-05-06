""" Realice un algoritmo que permita adivinar un número preestablecido entre 1 y 10, 
dando al usuario tres intentos, e informando si adivino o fallo. (ciclos + condicionales) """

import random

numero_preestablecido = random.randint(1, 10)
intentos = 3
adivino = False

print("Adivina el número entre 1 y 10. Tienes 3 intentos.")

# CICLO WHILE

""" while intentos > 0:
    intento = int(input("Ingresa tu número: "))
    if intento == numero_preestablecido:
        print("¡Felicidades! Adivinaste el número.")
        
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Fallaste. Te quedan {intentos} intentos.")
        else:
            print(f"Lo siento, has perdido. El número era {numero_preestablecido}.") """

# CICLO FOR

for intento in range(1, 4):
    numero = int(input(f"Intento {intento}/3 - Adivina el número (1 al 10): "))

    if numero == numero_preestablecido:
        print("¡Felicidades! Adivinaste el número.")
        adivino = True
        break
    else:
        print("Incorrecto.")

if not adivino:
    print(f"Lo siento, fallaste. El número era {numero_preestablecido}.")