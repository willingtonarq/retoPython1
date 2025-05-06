#Ejercicio #29 (Calcular la suma de todos los elementos de una lista en sus posiciones impares).

#
lista = []
suma = 0
posiciones_impares = []

n = int(input("Ingrese el número de elementos de la lista: "))
for i in range(n):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))
    lista.append(elemento)
    if i % 2 != 0:
        suma += elemento
        posiciones_impares.append(i)

    print(f"Elemento {i + 1}: {elemento}")
    print(f"Lista: {lista}")
    print(f"Posiciones impares: {posiciones_impares}")
    print(f"Suma de elementos en posiciones impares: {suma}")

    