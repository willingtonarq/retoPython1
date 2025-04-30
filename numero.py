'''Diseñe un programa que calcule e imprima el número de segundos que hay en un 
determinado número de días.'''
# Solicitar al usuario la cantidad de días
dias = int(input("Ingrese la cantidad de días: "))

# Calcular el número de segundos en esos días
segundos = dias * 24 * 60 * 60

# Mostrar el resultado
print(f"En {dias} día(s) hay {segundos} segundos.")
