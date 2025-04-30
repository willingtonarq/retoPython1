'''Construya un programa tal que dados los datos enteros A y B, escriba el resultado 
de la siguiente expresión: 
(A + B)2 
3 '''

# Solicitar los dos números enteros A y B
A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))

# Calcular la expresión (A + B)^2 / 3
resultado = ((A + B) ** 2) / 3

# Mostrar el resultado
print(f"El resultado de la expresión es: {resultado}")
