""" Implementar un algoritmo que calcule el producto de dos números enteros (n*m) 
haciendo sólo sumas.  """

n = int(input("Ingrese el primer número (n): "))
m = int(input("Ingrese el segundo número (m): "))
producto = 0
i = 0

# CICLO FOR

for i in range(m):
    producto += n

# CICLO WHILE

""" while i < m:
    producto += n
    i += 1 """

print(f"El producto de {n} y {m} es: {producto}")