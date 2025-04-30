'''Determinar si un número dado por el usuario es positivo o negativo'''-1
# Solicita al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

# Verifica si el número es positivo o negativo
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
