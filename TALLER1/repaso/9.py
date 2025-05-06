# Diseñar un programa que lea cuatro valores y calcule e imprima su producto, su 
# suma y su promedio.

valor1 = input("Ingresa el valor 1: ")
valor1 = int(valor1)

valor2 = input("Ingresa el valor 2: ")
valor2 = int(valor2)

valor3 = input("Ingresa el valor 3: ")
valor3 = int(valor3)

valor4 = input("Ingresa el valor 4: ")
valor4 = int(valor4)

producto = valor1 * valor2 * valor3 * valor4
print(f"El producto de los valores es {producto}")

suma = valor1 + valor2 + valor3 + valor4
print(f"La suma de los valores es {suma}")

promedio = (valor1 + valor2 + valor3 + valor4) / 4
print(f"El promedio de los valores es {promedio}")