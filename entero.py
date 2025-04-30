'''Determinar si un número entero dado por el usuario es par o impar'''

# Solicita al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Verifica si el número es par o impar
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
