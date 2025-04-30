# Solicitar al usuario un número
numero = float(input("Ingrese un número: "))

# Determinar si es positivo o negativo
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")