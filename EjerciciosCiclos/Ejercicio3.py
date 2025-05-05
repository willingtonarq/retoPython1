#Escribir un algoritmo que calcule la suma de los números enteros de n a m, siendo m>n,
# Utilizando el algoritmo del ejercicio 1. Los valores de n y m son dados por el usuario.

# Con while
n = int(input("Introduce el valor de n: "))
m = int(input("Introduce el valor de m (m > n): "))

suma = 0
i = n
while i <= m:
    suma += i
    i += 1
print(f"La suma de los números enteros de {n} a {m} es: {suma}")


# Con for
suma = 0
for i in range(n, m + 1):
    suma += i
print(f"La suma de los números enteros de {n} a {m} es: {suma}")


