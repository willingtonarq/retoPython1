#Ejercicio #03 (Escribir un programa que calcule el área de un círculo. Area= radio*radio*Pi).

# Leer el radio del círculo
radio = float(input("Por favor, ingrese el radio del círculo (en cm): "))
pi = 3.14159
area_circulo = pi * (radio ** 2)

print(f"\nEl área del círculo es: {area_circulo} cm²")

