""" Buscar en una lista de elementos numéricos, los elementos mayores a un valor X 
dado por el usuario y mostrar cuantos se encontraron. """

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mayor = int(input("Ingrese el valor de X: "))
contador = 0

for i in range(len(lista)):
    if lista[i] > mayor:
        contador += 1
print(f"Se encontraron {contador} elementos mayores a {mayor}.")