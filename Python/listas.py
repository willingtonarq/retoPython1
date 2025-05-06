# 1. Calcular el producto de todos los elementos de una lista de n posiciones.
lista = []
n = int(input("Ingrese el número de elementos de la lista: "))
producto = 1    
for i in range(n):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))
    lista.append(elemento)
    producto *= elemento
print("El producto de los elementos de la lista es:", producto)

# 2. Calcular la suma de todos los elementos de una lista de n posiciones.
array = []
n = int(input("Ingrese el número de elementos de la lista: "))
sumar =0 
for i in range(n):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))
    array.append(elemento)
    sumar += elemento
print("La suma de los elementos de la lista es:", sumar)
# 3. Buscar en una lista de elementos numéricos, los elementos mayores a un valor X
# dado por el usuario y mostrar cuantos se encontraron.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = int(input("Ingrese el valor de X: "))
cont = 0
for i in range(len(numeros)):
    if numeros[i] > x:
        cont += 1
print("Se encontraron", cont, "elementos mayores a", x)

# 4. Calcular la suma de todos los elementos de una lista en sus posiciones impares.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_impares = 0
for i in range(1, len(numeros), 2):
    suma_impares += numeros[i]
print("La suma de los elementos en posiciones impares es:", suma_impares)
# 5. Contar en una lista de elementos numéricos cuantos elementos son positivos, cuantos
# negativos y cuantos son cero.
lista = [1, -2, 3, 0, -4, 5, 0, -6]
positivos = 0
negativos = 0
cero = 0
for i in range(len(lista)):
    if lista[i] > 0:
        positivos += 1
    elif lista[i] < 0:
        negativos += 1
    else:
        cero += 1
print("Cantidad de elementos positivos:", positivos)
print("Cantidad de elementos negativos:", negativos)
print("Cantidad de ceros:", cero)
# 6. Calcular los cuadrados de todos los elementos de una lista.
numeros = [1, 2, 3, 4, 5]
cuadrados = []
for i in range(len(numeros)):
    cuadrados.append(numeros[i] ** 2)
print("Los cuadrados de los elementos de la lista son:", cuadrados)
# 7. Determinar si un número X dado por el usuario se encuentra repetido o no en una lista
# de elementos numéricos.
repetidos = [1, 2, 3, 4, 5, 1, 2, 3]
x = int(input("Ingrese el número a buscar: "))
encontrado = False
for i in range(len(repetidos)):
    if repetidos[i] == x:
        encontrado = True
        print("El número", x, "se encuentra repetido en la lista.")
        break
# 8. Buscar en una lista de elementos numéricos los elementos menores a un valor X dado
# por el usuario y mostrar las posiciones donde están ubicados.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = int(input("Ingrese el valor de X: "))
posiciones = []
for i in range(len(numeros)):
    if numeros[i] < x:
        posiciones.append(i)
print("Las posiciones de los elementos menores a", x, "son:", posiciones)
