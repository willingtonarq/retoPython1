#Ejercicio #07 (Construya un programa tal que dados los datos enteros A y B, escriba el resultado de la siguiente expresión: (A + B)2 / 3).

# Leer los valores de A y B
a = int(input("Por favor, ingrese el valor de A: "))
b = int(input("Por favor, ingrese el valor de B: "))

# Calcular el resultado de la expresión
result = ((a + b) ** 2) / 3
print(f"\nEl resultado de la expresión es: {result:.0f}")

