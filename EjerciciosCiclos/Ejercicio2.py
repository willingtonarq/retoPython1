#Escribir un algoritmo que calcule la suma de los cuadrados de los n primeros números
#naturales: 12 + 22 + 32 +… + n2

# Con For
n = int(input("Ingrese un número natural n: "))
suma = 0

for i in range(1, n + 1):
    suma += i**2

print(f"La suma de los cuadrados de los {n} primeros números naturales es: {suma}")



# Con While
n = int(input("Ingrese un número natural n: "))
suma = 0
i = 1

while i <= n:
    suma += i**2
    i += 1

print(f"La suma de los cuadrados de los {n} primeros números naturales es: {suma}")


