# Calcular la suma de todos los elementos de una lista de n posiciones.

lista = [1, 2, 3, 4, 5]
suma = 0

for i in range(len(lista)):
    suma += lista[i]
print(f"La suma de todos los elementos de la lista es: {suma}")