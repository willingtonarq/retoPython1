#Ejercicio #28 (Buscar en una lista de elementos numéricos, los elementos mayores a un valor X dado por el usuario y mostrar cuantos se encontraron).

lista = []
mayores = []

n = int(input("Ingrese el número de elementos de la lista: "))

for i in range(n):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))
    lista.append(elemento)
    
    print(f"Elemento {i + 1}: {elemento}")
    print(f"Lista: {lista}")

    print("")

x = int(input("Ingrese el valor de X: "))
print(f"Valor de X: {x}")
print("")

print("Elementos mayores a X:")
for i in range(n):
    if lista[i] > x:
        mayores.append(lista[i])
        print(f"Elemento mayor a X: {lista[i]}")

        print(f"Lista de elementos mayores a X: {mayores}")
        print("")

print(f"Cantidad de elementos mayores a X: {len(mayores)}")
print(f"Lista de elementos mayores a X: {mayores}")
print("")