#Ejercicio #14 (Un año es bisiesto si es divisible por 4 y no es divisible por 100, o es bisiesto si es divisible por 400. Escribir un algoritmo que lea un año y devuelva si es bisiesto o no).

Año = int(input("Introduce un año: "))

if (Año % 4 == 0 and Año % 100 != 0) or (Año % 400 == 0):
    print("El año", Año, "es bisiesto.")
else:
    print("El año", Año, "no es bisiesto.")

print("Fin del programa")

