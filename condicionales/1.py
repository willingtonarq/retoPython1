# Determinar si un número entero dado por el usuario es par o impar

num = input("Introduce un número: ")
num = int(num)

if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")