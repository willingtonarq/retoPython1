#Ejercicio #24 (Realice un algoritmo que solicite sólo números positivos, muestre su suma y promedio, hasta que el usuario digite 0, o digite un número negativo. (ciclos + condicionales).

suma = 0  # Inicializamos la suma en 0
contador = 0  # Inicializamos el contador de números positivos en 0
numero = 0  # Inicializamos la variable numero en 0

while True:
    # Pedimos al usuario que ingrese un número
    numero = float(input("Ingrese un número positivo (0 para salir): "))

    # Verificamos si el número es 0 o negativo
    if numero <= 0:
        break  # Salimos del bucle si el número es 0 o negativo

    # Sumamos el número a la suma total
    suma += numero
    # Incrementamos el contador de números positivos
    contador += 1

    print(f"La suma de los números positivos ingresados es: {suma}")
    # Verificamos si se ingresaron números positivos para evitar división por cero
    if contador > 0:
        promedio = suma / contador  # Calculamos el promedio
        print(f"El promedio de los números positivos ingresados es: {promedio}")
    else:
        print("No se ingresaron números positivos para calcular el promedio.")


