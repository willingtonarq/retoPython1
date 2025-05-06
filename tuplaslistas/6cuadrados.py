#Calcular los cuadrados de todos los elementos de una lista.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista) #inicializa la lista

cuadrados = []

for i in range(len(lista)):
    cuadrados.append(lista[i]**2) #agrega el cuadrado de cada elemento a la lista
print("Los cuadrados de los elementos de la lista son:", cuadrados) #imprime la lista de cuadrados


