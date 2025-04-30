# Diseñe un programa que calcule e imprima el número de segundos que hay en un 
# determinado número de días. 

dias = input("Ingresa el número de días: ")
dias = int(dias)

# El número total de segundos por día es de 86.400
segundos = (60 * 60 * 24 * dias)
print(f"El número {dias} de días en segundos es {segundos}")