#Diseñar un programa que lea cuatro valores y calcule e imprima su producto, su suma y su promedio.


# Ejercicio 9 (4 valores) suma = A + B + C + D; promedio = suma / 4
A = float(input("¿Cuál es el valor de A?")) 
B = float(input("¿Cuál es el valor de B?"))
C = float(input("¿Cuál es el valor de C?"))
D = float(input("¿Cuál es el valor de D?"))
suma = A + B + C + D
promedio = suma / 4
print(f"\nLa suma de los valores es: {suma}")
print(f"El promedio de los valores es: {promedio}")
