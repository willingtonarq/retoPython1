#Buscar en una lista de elementos numéricos los elementos menores a un valor X dado 
#por el usuario y mostrar las posiciones donde están ubicados.

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)
numero = int(input("Ingresa el número que quieres verificar: "))

posiciones = []

for i in range(len(lista)):
    if lista[i] < numero:
        posiciones.append(i)


if len(posiciones) > 0:
    print(f"Los números menores a {numero} están en las posiciones: {posiciones}")
else:
    print(f"No hay números menores a {numero} en la lista.")

