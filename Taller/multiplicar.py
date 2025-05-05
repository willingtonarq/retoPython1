#Escriba un algoritmo que genere y muestre la tabla de multiplicar de un número entero 
#positivo dado por el usuario.

#for 
""" numero = int(input("Ingresa un número entero positivo: "))

if numero > 0:
    for i in range(1, 11):  # Generar la tabla de multiplicar del 1 al 10
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Por favor ingresa un número entero positivo.") """

#while
numero = int(input("Ingresa un número entero positivo: "))

if numero > 0:
    i = 1
    while i <= 10:  # Generar la tabla de multiplicar del 1 al 10
        print(f"{numero} x {i} = {numero * i}")
        i += 1  # Incrementa 'i' en 1
else:
    print("Por favor ingresa un número entero positivo.")

