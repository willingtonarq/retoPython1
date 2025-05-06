# Un año es bisiesto si es divisible por 4 y no es divisible por 100, o es bisiesto si es divisible por 400. Escribir un algoritmo que lea un año y devuelva si es bisiesto o no.

anio = int(input("Ingresa el número del año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")