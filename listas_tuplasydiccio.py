'''
Calcular el producto de todos los elementos de una lista de n posiciones


producto_lista = [1, 2, 3, 4, 5]
producto = 1
for i in producto_lista:
    producto *= i
print("El producto de la lista es:", producto)



# Calcular la suma de todos los elementos de una lista de n posiciones.
suma_lista = [1, 2, 3, 4, 5]
suma = 0
for i in suma_lista:
    suma += i
print("La suma de la lista es:", suma)


'''
'''
Buscar en una lista de elementos numéricos, los elementos mayores a un valor X
dado por el usuario y mostrar cuantos se encontraron.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mayor_a = int(input("Ingrese un número: "))
contador = 0
for i in numeros:
    if i > mayor_a:
        contador += 1
print("Se encontraron", contador, "números mayores a", mayor_a)
'''

#Calcular la suma de todos los elementos de una lista en sus posiciones impares.
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = 0
for i in range(len(numeros)):
    if i % 2 != 0:
        suma += numeros[i]
print("La suma de los elementos en posiciones impares es:", suma)
'''
#Contar en una lista de elementos numéricos cuantos elementos son positivos, cuantos
#negativos y cuantos son cero.
'''
numeros = [1, -2, 3, 0, -5, 6, 0, -7, 8, 9]
positivos = 0
negativos = 0
cero = 0
for i in numeros:
    if i > 0:
        positivos += 1
    elif i < 0:
        negativos += 1
    else:
        cero += 1
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
print("Cantidad de ceros:", cero)
'''

#Calcular los cuadrados de todos los elementos de una lista

'''
numeros = [1, 2, 3, 4, 5]
cuadrados = []
for i in numeros:
    cuadrados.append(i ** 2)
print("Los cuadrados de los elementos de la lista son:", cuadrados)
'''

#Determinar si un número X dado por el usuario se encuentra repetido o no en una lista
#de elementos numéricos.

'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_a_buscar = int(input("Ingrese un número: ")) 
encontrado = False
for i in numeros:
    if i == numero_a_buscar:
        encontrado = True
        break
if encontrado:
    print("El número", numero_a_buscar, "se encuentra en la lista.")
else:
    print("El número", numero_a_buscar, "no se encuentra en la lista.")
'''

#Buscar en una lista de elementos numéricos los elementos menores a un valor X dado
#por el usuario y mostrar las posiciones donde están ubicados.


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
menor_a = int(input("Ingrese un número: "))
posiciones = []
for i in range(len(numeros)):
    if numeros[i] < menor_a:
        posiciones.append(i)
print("Las posiciones de los números menores a", menor_a, "son:", posiciones)
