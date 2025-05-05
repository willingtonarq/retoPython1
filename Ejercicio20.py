#Ejercicio #20 (Diseñar un algoritmo que calcule y muestre el promedio de cinco valores de temperaturas dadas por el usuario).

# Definimos la función para calcular el promedio de cinco temperaturas

def promedio_temperaturas(temperaturas):
    suma = sum(temperaturas)
    return suma / len(temperaturas)

# Programa principal
# Solicitar al usuario que ingrese cinco temperaturas
print("Este programa calcula el promedio de cinco temperaturas.")
temperaturas = []

for i in range(5):
    temp = float(input(f"Introduce la temperatura {i + 1}: "))
    temperaturas.append(temp)

print(f"El promedio de las temperaturas es: {promedio_temperaturas(temperaturas)}")
