#Diseñar un algoritmo que calcule y muestre el promedio de cinco valores de temperaturas dadas por el usuario.


# Con for
suma = 0

for i in range(5):
    temp = float(input(f"Ingrese la temperatura #{i + 1}: "))
    suma += temp  
promedio = suma / 5

print(f"El promedio de las 5 temperaturas es: {promedio}")


# Con while
suma = 0
contador = 0  
while contador < 5:
    temp = float(input(f"Ingrese la temperatura #{contador + 1}: "))
    suma += temp 
    contador += 1  
promedio = suma / 5
print(f"El promedio de las 5 temperaturas es: {promedio}")
