""" Escribir un algoritmo que calcule la suma de los cuadrados de los n primeros números naturales: 12 + 22 + 32 +… + n2.  """

n = int(input("Ingresa un número: "))
suma = 0
i = 1

# CICLO FOR
""" for i in range(1, n + 1):
    suma += i ** 2

print(f"La suma de los cuadrados de los primeros {n} números naturales es: {suma}")

"""

# CICLO WHILE

while i <= n:
    suma += i ** 2
    i += 1

print(f"La suma de los cuadrados de los primeros {n} números naturales es: {suma}")