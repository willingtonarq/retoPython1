# Calcular la suma de todos los elementos de una lista en sus posiciones impares.  

lista = [1, 2, 3, 4, 5, 6, 7]
suma = 0

for i in range(len(lista)):
    if i % 2 != 0:
        suma += lista[i]
print(f"La suma de todos los elementos de la lista en posiciones impares es: {suma}")