#Escriba un algoritmo que genere y muestre la tabla de multiplicar de un número entero
#positivo dado por el usuario


# Con for
numero = int(input("Ingrese un número entero positivo: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


# Con while
numero = int(input("Ingrese un número entero positivo: "))
i = 1

while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1
