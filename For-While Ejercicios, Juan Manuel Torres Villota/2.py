Num = int(input("Escriba un numero: "))
Contador = 0
Suma = 0

while Contador < Num:
    Suma += Contador **2
    Contador += 1

print("La suma de los numeros cuadrados anterior a ese es de ", Suma)   