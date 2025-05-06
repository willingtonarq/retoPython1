""" Buscar en una lista de elementos numéricos los elementos menores a un valor X dado por el usuario y mostrar las posiciones donde están ubicados. """

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
menor = int(input("Ingrese el valor de X: "))
contador = 0

for i in range(len(lista)):
    if lista[i] < menor:
        contador += 1
print(f"Se encontraron {contador} elementos mayores a {menor}.")