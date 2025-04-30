# Leer los cuatro valores
valor1 = float(input("Ingrese el primer valor: "))
valor2 = float(input("Ingrese el segundo valor: "))
valor3 = float(input("Ingrese el tercer valor: "))
valor4 = float(input("Ingrese el cuarto valor: "))

# Calcular suma, producto y promedio
suma = valor1 + valor2 + valor3 + valor4
producto = valor1 * valor2 * valor3 * valor4
promedio = suma / 4

# Mostrar los resultados
print("La suma es:", suma)
print("El producto es:", producto)
print("El promedio es:", round(promedio, 2))