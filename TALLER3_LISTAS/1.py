# Calcular el producto de todos los elementos de una lista de n posiciones. 

lista = [1, 2, 3, 4, 5]
producto = 1

for i in range(len(lista)):
    producto *= lista[i]
print("El producto de todos los elementos de la lista es:", producto)