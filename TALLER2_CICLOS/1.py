""" Escribir un algoritmo que calcule la suma de los n primeros números naturales. 
Analizar si se puede implementar con los dos tipos de ciclos. El valor de n es dado por el usuario.  """

# CICLO FOR
n = int(input("Ingrese un número: "))
suma = 0
i = 1

""" for i in range(1, n + 1):
    suma += i

print(f"La suma de los primeros {n} números naturales es: {suma}") """

# CICLO WHILE 

while i <= n:
    suma += i
    i += 1

print(f"La suma de los primeros {n} números naturales es: {suma}")