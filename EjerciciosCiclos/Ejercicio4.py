#Implementar un algoritmo que calcule el producto de dos números enteros (n*m)
#haciendo sólo sumas.


# Con while
n = int(input("Ingrese el primer número (n): "))
m = int(input("Ingrese el segundo número (m): "))

producto = 0
i = 0
while i < abs(m):
    producto += n
    i += 1
producto = producto if m >= 0 else -producto
print(f"El producto de {n} y {m} es: {producto}")


# Con for
producto = 0

for i in range(abs(m)):
    producto += n
producto = producto if m >= 0 else -producto
print(f"El producto de {n} y {m} es: {producto}")

