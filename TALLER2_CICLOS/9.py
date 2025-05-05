""" Realice un algoritmo que solicite sólo números positivos, muestre su suma y promedio, hasta que el usuario digite 0, o digite un número negativo. (ciclos + condicionales).  """

suma = 0
contador = 0

# CICLO WHILE
""" while True:
    numero = float(input("Ingrese un número positivo (0 para salir): "))
    if numero < 0:
        break
    elif numero == 0:
        break
    suma += numero
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"La suma de los números ingresados es: {suma}")
    print(f"El promedio de los números ingresados es: {promedio}")
else:
    print("No se ingresaron números positivos.") """

# CICLO FOR
for _ in iter(int, 1):
    numero = float(input("Ingrese un número positivo (0 para salir): "))
    if numero <= 0:
        break
    suma += numero
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"La suma de los números ingresados es: {suma}")
    print(f"El promedio de los números ingresados es: {promedio}")
else:
    print("No se ingresaron números positivos.")
