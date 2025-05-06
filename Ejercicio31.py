#Ejercicio #31 (Calcular los cuadrados de todos los elementos de una lista).

numeros = [1, 2, 3, 4, 5]
cuadrados = []

for numero in numeros:
    cuadrado = numero ** 2
    cuadrados.append(cuadrado)

print("La lista original es:", numeros)
print("Los cuadrados de los elementos de la lista son:", cuadrados)



