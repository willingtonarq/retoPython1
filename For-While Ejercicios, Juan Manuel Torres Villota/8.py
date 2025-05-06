from random import randint

numRandom = randint(0, 10)
intentos = 3
print("Solo tienes 3 intentos para adivinar el numero")

while intentos > 0:
    Adivinar = int(input("Adivina el numero: "))
    
    if Adivinar == numRandom:
        print("Felicidades, adivinaste")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Te quedan {intentos} intentos")
        else:
            print("Game over")

if intentos == 0:
    print(f"Fallaste, el numero era {numRandom}")    

       



