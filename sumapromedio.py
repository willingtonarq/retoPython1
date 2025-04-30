'''Diseñar un programa que lea cuatro valores y calcule e imprima su producto, su 
suma y su promedio.'''

# Solicitar los 4 valores al usuario
valor1 = float(input("Ingrese el primer valor: "))
valor2 = float(input("Ingrese el segundo valor: "))
valor3 = float(input("Ingrese el tercer valor: "))
valor4 = float(input("Ingrese el cuarto valor: "))

# Calcular la suma
suma = valor1 + valor2 + valor3 + valor4

# Calcular el producto
producto = valor1 * valor2 * valor3 * valor4

# Calcular el promedio
promedio = suma / 4

# Mostrar los resultados
print(f"La suma es: {suma}")
print(f"El producto es: {producto}")
print(f"El promedio es: {promedio}")
