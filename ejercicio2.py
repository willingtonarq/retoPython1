#Escribir un programa que calcule el área de un círculo.
#Area= radio*radio*Pi
import math

radio = float(input("Ingrese el radio del circulo: "))
area_circulo = math.pi * radio ** 2
print(f"Área del circulo: {area_circulo}")
