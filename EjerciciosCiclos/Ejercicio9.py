#Realice un algoritmo que solicite sólo números positivos, muestre su suma y promedio,
#hasta que el usuario digite 0, o digite un número negativo. (ciclos + condicionales).




# Con while
suma = 0
contador = 0
num = float(input("Ingrese un número positivo (0 o negativo para salir): "))

while num > 0:
    suma += num
    contador += 1
    num = float(input("Ingrese otro número positivo (0 o negativo para salir): "))

if contador > 0:
    promedio = suma / contador
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
else:
    print("No se ingresaron números positivos.")


#Con for
suma = 0
contador = 0

for _ in range(1000):  
    num = float(input("Ingrese un número positivo (0 o negativo para salir): "))

    if num <= 0:
        break  
    suma += num
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
else:
    print("No se ingresaron números positivos.")
  
