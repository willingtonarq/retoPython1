""" Diseñar un algoritmo que calcule y muestre el promedio de cinco valores de 
temperaturas dadas por el usuario.  """

temperaturas = []
suma = 0

for i in range(5):
    temp = float(input(f"Ingrese la temperatura {i + 1}: "))
    temperaturas.append(temp)
    suma += temp

promedio = suma / len(temperaturas)
print(f"El promedio de las temperaturas es: {promedio}")