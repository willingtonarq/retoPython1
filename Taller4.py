# 1. Calcular el producto de todos los elementos de una lista de n posiciones.
producto = 1
n = int(input("Ingrese el número de elementos de la lista: "))
lista = []
for i in range(n):
    elemento = int(input("Ingrese el elemento " + str(i + 1) + ": "))
    lista.append(elemento)
    producto *= elemento
print("El producto de todos los elementos de la lista es:", producto)

# 2. Calcular la suma de todos los elementos de una lista de n posiciones.
suma = 0
n = int(input("Ingrese el número de elementos de la lista: "))
lista = []
for i in range(n):
    elemento = int(input("Ingrese el elemento " + str(i + 1) + ": "))
    lista.append(elemento)
    suma += elemento
print("La suma de todos los elementos de la lista es:", suma)

# 3. Buscar en una lista de elementos numéricos, los elementos mayores a un valor X
# dado por el usuario y mostrar cuantos se encontraron.

lista = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
x = int(input("Ingrese un valor X desde 11: "))
contador = 0
for i in lista:
    if i > x:
        contador += 1
print("Se encontraron", contador, "elementos mayores a", x)

# 4. Calcular la suma de todos los elementos de una lista en sus posiciones impares.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_impares = 0
for i in range(1, len(lista), 2):
    suma_impares += lista[i]
print("La suma de los elementos en posiciones impares es:", suma_impares)

# 5. Contar en una lista de elementos numéricos cuantos elementos son positivos, cuantos
# negativos y cuantos son cero.
lista = [1, -2, -3, 0, -5, -6, 0, -7]
contador_positivos = 0
contador_negativos = 0
contador_ceros = 0
for i in lista:
    if i > 0:
        contador_positivos += 1
    elif i < 0:
        contador_negativos += 1
    else:
        contador_ceros += 1
print("Cantidad de elementos positivos:", contador_positivos)

# 6. Calcular los cuadrados de todos los elementos de una lista.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [i ** 2 for i in lista]
print("Los cuadrados de los elementos de la lista son:", squares)

# 7. Determinar si un número X dado por el usuario se encuentra repetido o no en una lista
# de elementos numéricos.
x = int(input("Ingrese un número X: "))
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
contador = 0
for i in lista:
    if i == x:
        contador += 1
if contador > 0:
    print("El número", x, "se encuentra repetido", contador, "veces en la lista.")

# 8. Buscar en una lista de elementos numéricos los elementos menores a un valor X dado
# por el usuario y mostrar las posiciones donde están ubicados.
x = int(input("Ingrese un valor X: "))
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
posiciones = []
for i in range(len(lista)):
    if lista[i] < x:
        posiciones.append(i)
print("Las posiciones de los elementos menores a", x, "son:", posiciones)