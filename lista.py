











"""1. Calcular el producto de todos los elementos de una lista de n posiciones."""
# # Inicializar la lista y el producto
lista = []
producto = 1
# # Leer los elementos de la lista
n = int(input("Ingrese el número de elementos de la lista: "))
for i in range(n):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))
    lista.append(elemento)
# # Calcular el producto
for i in range(n):
    producto *= lista[i]
# # Mostrar el resultado
print(f"El producto de los elementos de la lista es: {producto}")


"""2. Calcular la suma de todos los elementos de una lista de n posiciones."""

# # Inicializar la lista y el producto
lista = []
suma = 0
# # Leer los elementos de la lista
n = int(input("Ingrese el número de elementos de la lista: "))
for i in range(n):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))
    lista.append(elemento)
# # Calcular el producto
for i in range(n):
    suma += lista[i]
# # Mostrar el resultado
print(f"la suma de los elementos de la lista es: {suma}")

"""Buscar en una lista de elementos numéricos, los elementos mayores a un valor X
    dado por el usuario y mostrar cuantos se encontraron."""

# # Inicializar la lista y el producto
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero = int(input("Ingrese el numero base para buscra los mayores : "))
# # Leer los elementos de la lista
contador = 0
for i in lista:
    if lista[i] > numero:
        contador += 1
# # Mostrar el resultado
print(f"la cantidad de elementos mayores a {numero} es: {contador}")


"""4. Calcular la suma de todos los elementos de una lista en sus posiciones impares."""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = 0

for i in lista:
    if  i % 2 != 0:
        suma += lista[i]
# # Mostrar el resultado   
print(f"la suma de los elementos en posiciones impares es: {suma}") 



"""Contar en una lista de elementos numéricos cuantos elementos son positivos, cuantos
negativos y cuantos son cero."""

# # Inicializar la lista y el producto
lista = [1, 2, 3, -4, -5, 0, 6, -7, 8, 9]
contador_positivos = 0
contador_negativos = 0
contador_ceros = 0
# # Leer los elementos de la lista
for i in lista:
    if i > 0:
        contador_positivos += 1
    elif i < 0:
        contador_negativos += 1
    else:
        contador_ceros += 1
# # Mostrar el resultado
print(f"la cantidad de elementos positivos es: {contador_positivos}")
print(f"la cantidad de elementos negativos es: {contador_negativos}") 
print(f"la cantidad de elementos cero es: {contador_ceros}")      


"""6. Calcular los cuadrados de todos los elementos de una lista."""

# # Inicializar la lista y el producto
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Leer los elementos de la lista
cuadrados = []
for i in lista:
    cuadrados.append(i ** 2)
# # Mostrar el resultado
print(f"los cuadrados de los elementos de la lista son: {cuadrados}")



"""Determinar si un número X dado por el usuario se encuentra repetido o no en una lista
de elementos numéricos."""

lista = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero = int(input("Ingrese el numero a buscar: "))
contador = 0

for i in lista:
    if i == numero:
        contador += 1
        print(f"el numero {numero} se encuentra {contador} veces en la lista")
    else:
        print(f"el numero {numero} no se encuentra en la lista")


"""8. Buscar en una lista de elementos numéricos los elementos menores a un valor X dado
por el usuario y mostrar las posiciones donde están ubicados."""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero = int(input("Ingrese el numero base para buscra los menores : "))

for i in range(len(lista)):
    if lista[i] < numero:
        print(f"el numero {lista[i]} se encuentra en la posicion {i} de la lista")