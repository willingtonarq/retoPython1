#Escribir un programa que calcule el área de un círculo. Area= radio*radio*Pi

# Ejercicio 3 (area circulo)= Area = pi * radio^2
radio = float(input("por favor, introduce el radio del círculo: "))
import math # Importar la librería math para usar pi
area_circulo = math.pi * (radio ** 2)
print(f"\nEl área del círculo es: {area_circulo} cm²")