#Realice un algoritmo que permita adivinar un número preestablecido entre 1 y 10,
#dando al usuario tres intentos, e informando si adivino o fallo. (ciclos + condicionales)

#Con While
secreto = 7
intento = 1
acertado = False

while intento <= 3:
    adivina = int(input(f"Intento #{intento}: Adivina el número (1 al 10): "))

    if adivina == secreto:
        print("¡Adivinaste el número!")
        acertado = True
        break 
    else:
        print("Incorrecto.")
    
    intento += 1

if not acertado:
    print("Fallaste los 3 intentos.")


# Con For
secreto = 7

for intento in range(1, 4):
    adivina = int(input(f"Intento #{intento}: Adivina el número (1 al 10): "))

    if adivina == secreto:
        print("¡Adivinaste el número!")
        break  
    else:
        print("Incorrecto.")

else:
    print("Fallaste los 3 intentos.")


