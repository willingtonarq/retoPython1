""" Calcular y visualizar la suma y el producto de los números pares comprendidos entre 20 y 400 ambos inclusive.  """

suma = 0
producto = 1

# CICLO FOR

""" for i in range(20, 401, 2):
    suma += i
    producto *= i

print(f"La suma de los números pares es: {suma}")
print(f"El producto de los números pares es: {producto}")
 """
# CICLO WHILE

numero = 20
while numero <= 400:
    suma += numero
    producto *= numero
    numero += 2

print(f"La suma de los números pares es: {suma}")
print(f"El producto de los números pares es: {producto}")
