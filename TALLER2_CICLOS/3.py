""" Escribir un algoritmo que calcule la suma de los números enteros de n a m, siendo 
m>n, utilizando el algoritmo del ejercicio 1. Los valores de n y m son dados por el  usuario.  """

n = int(input("Ingrese el valor de n: "))
m = int(input("Ingrese el valor de m: "))
suma = 0
i = 1

# CICLO FOR

""" if m > n:
    suma = 0
    for i in range(1, m + 1):
        suma += i
    print(f"La suma de los números enteros de {n} a {m} es: {suma}")
else:
    print("Error: el valor de m debe ser mayor que n.") """

# CICLO WHILE

while i <= m:
    if(m > n):
        suma += i
    else:
        print("El valor de m debe ser mayor que n.")
        break
    i += 1

print(f"La suma de los números enteros de {n} a {m} es: {suma}")