Lista = [1, 1, 2, 3, 4, 5, 6, 5, 5]
Contador = 0
valorX = int(input("Escriba el numero que se repite "))

for i in Lista:
    if valorX == i:
        Contador += 1

print("El numero", valorX, "se encuentra", Contador, "vez/veces en la lista")
