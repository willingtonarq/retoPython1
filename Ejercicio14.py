#Un año es bisiesto si es divisible por 4 y no es divisible por 100, o es bisiesto si es
#divisible por 400. Escribir un algoritmo que lea un año y devuelva si es bisiesto o no.

# Ejercicio 14 (año bisiesto divisibilidad por 4 y no 100 o divisibilidad por 400)

año = int(input("Introduce un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"\nEl año {año} es bisiesto.")
else:
    print(f"\nEl año {año} no es bisiesto.")
