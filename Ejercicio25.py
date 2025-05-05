#Ejercicio #25 (Escriba un algoritmo que genere y muestre la tabla de multiplicar de un número entero positivo dado por el usuario).

numero = 0  # Inicializamos la variable numero en 0
suma = 0  # Inicializamos la suma en 0
producto = 1  # Inicializamos el producto en 1 para evitar multiplicar por 0

# Definimos la función para generar la tabla de multiplicar
def generar_tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")

    # Usamos un bucle for para iterar desde 1 hasta 10
    for i in range(1, 11):  # Generamos la tabla del 1 al 10
        resultado = numero * i  # Calculamos el resultado de la multiplicación
        print(f"{numero} x {i} = {resultado}")  # Imprimimos el resultado

# Pedimos al usuario que ingrese un número entero positivo
numero = int(input("Ingrese un número entero positivo para generar su tabla de multiplicar: ")) 

print(f"Tabla de multiplicar del {numero}:")
# Llamamos a la función para generar la tabla de multiplicar
generar_tabla_multiplicar(numero)  # Llamamos a la función para generar la tabla de multiplicar
