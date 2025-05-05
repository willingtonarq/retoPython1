""" Escriba un algoritmo que genere y muestre la tabla de multiplicar de un número entero positivo dado por el usuario.  """

numero = int(input("Ingrese un número entero positivo: "))

# CICLO FOR

""" if numero > 0:
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Por favor, ingrese un número entero positivo.") """

# CICLO WHILE
if numero > 0:
    print(f"Tabla de multiplicar del {numero}:")
    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i += 1
else:
    print("Por favor, ingrese un número entero positivo.")
