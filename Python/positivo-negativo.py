#determinar si un numero es negativo o positivo
numero = int(input("Ingrese un número: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:    
    print("El número es negativo.")
else:
    print("El número es cero.")