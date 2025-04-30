import math

# Escribir un programa que calcule el área de un círculo.  
# Area= radio*radio*Pi 


radio = input("Ingresa el valor del radio: ")
radio = int(radio)

area = math.pi * (radio ** 2)
print(f"El area del circulo es {area}")