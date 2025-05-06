#Ejercicio #32 (Determinar si un número X dado por el usuario se encuentra repetido o no en una lista de elementos numéricos).

numeros = [1, 1, 2, 4, 2, 6, 7, 8, 1, 0, 1, 2, 3, 7, 5, 6, 7, 8, 9]
numero = int(input("Ingrese un número: "))

for num in numeros:
    if num == numero:
        if numeros.count(numero) > 1:
            print(f"El número {numero} se encuentra repetido {numeros.count(numero)} veces en la lista.")
            break
        else:
            print(f"El número {numero} no se encuentra repetido en la lista.")
        break
