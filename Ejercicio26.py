# Ejercicio #26 (Calcular el producto de todos los elementos de una lista de n posiciones).

lista = []
producto = 1
n = int(input("Ingrese el número de elementos de la lista: "))

while n <= 0:
    print("El número de elementos debe ser mayor que cero.")
    n = int(input("Ingrese el número de elementos de la lista: "))

for i in range(n):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))
    lista.append(elemento)
    producto *= elemento

    print(f"Elemento {i + 1}: {elemento}")

print(f"Lista: {lista}")
print(f"Producto de los elementos de la lista: {producto}")

