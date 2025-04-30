# Un año es bisiesto si es divisible por 4 y no es divisible por 100, o es bisiesto si es
# divisible por 400. Escribir un algoritmo que lea un año y devuelva si es bisiesto o no.
año = int(input("Ingrese un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")