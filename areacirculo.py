"""Escribir un programa que calcule el área de un círculo.  
Area= radio*radio*Pi

# Importar la constante Pi de la biblioteca math
from math import pi
# Definir la función para calcular el área del círculo
def area_circulo(radio):
    return pi * radio * radio
# Definir la función principal
def main():
    # Solicitar al usuario que introduzca el radio del círculo
    radio = float(input("Introduce el radio del círculo: "))
    # Calcular el área utilizando la función definida
    area = area_circulo(radio)
    # Mostrar el resultado al usuario
    print(f"El área del círculo es: {area}")
# Llamar a la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()
# El programa calcula el área de un círculo dado su radio.
# El área se calcula utilizando la fórmula A = π * r^2, donde π es la constante Pi y r es el radio del círculo.
# El resultado se muestra en la consola."""

from math import pi
def area_circulo(radio):
    return pi * radio * radio
def main():
    radio = float(input("Introduce el radio del círculo: "))
    area = area_circulo(radio)
    print(f"El área del círculo es: {area}")
if __name__ == "__main__":
    main()