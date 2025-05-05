#Ejercicio #22 (Calcular y visualizar la suma y el producto de los números pares comprendidos entre 20 y 400 ambos inclusive).

# Definimos la función para calcular la suma y el producto de los números pares
suma = 0
producto = 1  # Inicializamos el producto en 1 para evitar multiplicar por 0
for numero in range(20, 401):
    if numero % 2 == 0:  # Verificamos si el número es par
        suma += numero  # Sumamos el número par a la suma total
        producto *= numero  # Multiplicamos el número par al producto total

print(f"La suma de los números pares entre 20 y 400 es: {suma}")
print(f"El producto de los números pares entre 20 y 400 es: {producto}")

