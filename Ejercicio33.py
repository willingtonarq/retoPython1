#Ejercicio #33 (Buscar en una lista de elementos numéricos los elementos menores a un valor X dado por el usuario y mostrar las posiciones donde están ubicados).

Lista = [1,2,3,4,5,6,7,8,9,10]
menores = []
valor = int(input("Ingrese un valor: "))
posiciones = []

for i in range(len(Lista)):
    if Lista[i] < valor:
        menores.append(Lista[i])
        posiciones.append(i)

print(f"Los elementos menores a {valor} son: {menores}")
print(f"Las posiciones de los elementos menores a {valor} son: {posiciones}")
