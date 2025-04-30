#Ejercicio #09 (Diseñar un programa que lea cuatro valores y calcule e imprima su producto, su suma y su promedio).

# Leer los cuatro valores
valor1 = float(input("Por favor, ingrese el primer valor: "))
valor2 = float(input("Por favor, ingrese el segundo valor: "))
valor3 = float(input("Por favor, ingrese el tercer valor: "))
valor4 = float(input("Por favor, ingrese el cuarto valor: "))

# Calcular el producto, la suma y el promedio
producto = valor1 * valor2 * valor3 * valor4
suma = valor1 + valor2 + valor3 + valor4
promedio = suma / 4

print(f"\nEl producto de los valores es: {producto:.3f}")
print(f"La suma de los valores es: {suma:.3f}")
print(f"El promedio de los valores es: {promedio:.3f}")
