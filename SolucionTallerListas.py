#Para los siguientes ejercicios, después ANALIZAR y de hallar la solución al problema,
#desarrolle su correspondiente programa utilizando según el caso estructuras repetitivas
#y/o listas.
#1. Calcular el producto de todos los elementos de una lista de n posiciones.
""" producto = 1
dato = 1
numeros = []
while dato != 0:
    dato = input("Ingrese un numero para agregarlo a la lista o 0 pa salir: ")
    dato = int(dato)
    if dato != 0:
        numeros.append(dato)
        print(numeros)    

for numero in numeros:
    producto *= numero

print(f"El producto de la lista es: {producto}") """

#2. Calcular la suma de todos los elementos de una lista de n posiciones.
""" suma = 0
dato = 1
numeros = []
while dato != 0:
    dato = input("Ingrese un numero para agregarlo a la lista o 0 pa salir: ")
    dato = int(dato)
    if dato != 0:
        numeros.append(dato)
        print(numeros)    

for numero in numeros:
    suma += numero

print(f"La suma de la lista es: {suma}") """

#3. Buscar en una lista de elementos numéricos, los elementos mayores a un valor X
#dado por el usuario y mostrar cuantos se encontraron.
""" numeros = [1,2,3,4,5,6,7,8,9,10]
valor = input("Ingrese un valor para determinar cuantos valores mayores existe: ")
valor = int(valor)
repeticiones = 0

for numero in numeros:
    if numero > valor:
        print(numero, " ", valor)
        repeticiones += 1

print(f"la cantidas de valores mayores a {valor} son {repeticiones}") """

#4. Calcular la suma de todos los elementos de una lista en sus posiciones impares.
""" numeros = [0,1,3,6,6,5,2]
suma = 0
contador = 0

while contador != len(numeros):
    if contador%2 != 0:
        suma += numeros[contador]
    contador += 1
        
print(f"la suma de la posiciones impares son: {suma}") """

#5. Contar en una lista de elementos numéricos cuantos elementos son positivos, cuantos
#negativos y cuantos son cero.
""" numeros = [0,1,2,3,4,-4,-3,-2,0]
ceros = 0
positivos = 0
negativos = 0

for numero in numeros:
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1
    else:
        ceros += 1

print(f"Cantidad ceros: {ceros} \nCantidad positivos: {positivos} \nCantidad negativos: {negativos}")
 """

#6. Calcular los cuadrados de todos los elementos de una lista.
""" numeros = [0,2,4,3,6]

for numero in numeros:
    print(f"Cuadrado de {numero} = {numero**2}") """

#7. Determinar si un número X dado por el usuario se encuentra repetido o no en una lista
#de elementos numéricos.
""" numeros = [3,5,2,1,1,3,6,3]

numero = input("Ingrese un valor para comprobar si esta repetido: ")
numero = int(numero)
repeticiones = numeros.count(numero)

if repeticiones > 1:
    print(f"el numero {numero} esta repetido {repeticiones-1} veces")
elif repeticiones == 1:
    print(f"El numero {numero} no se repite")
else:
    print(f"El numero {numero} no aparece en la lista") """

#8. Buscar en una lista de elementos numéricos los elementos menores a un valor X dado
#por el usuario y mostrar las posiciones donde están ubicados.
""" numeros = [3,5,2,1,4,1,3,6,3]

valor = input("Ingrese un valor para buscar los elmentos menores y su posicion: ")
valor = int(valor)

for i in range(len(numeros)):
    if numeros[i] < valor:
        print(f"Valor: {numeros[i]} \nPosicion: {i}") """
        
