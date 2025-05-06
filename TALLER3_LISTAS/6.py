#  Calcular los cuadrados de todos los elementos de una lista. 

lista = [1, 2, 3, 4, 5]
cuadrados = []

for i in range(len(lista)):
    cuadrados.append(lista[i] ** 2)
print("Los cuadrados de todos los elementos de la lista son:", cuadrados)