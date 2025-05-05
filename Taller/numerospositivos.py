#Realice un algoritmo que solicite sólo números positivos, muestre su suma y promedio, 
#hasta que el usuario digite 0, o digite un número negativo. (ciclos + condicionales).

#for

suma = 0
contador = 0

for i in range(10):  # Limitar a 10 intentos, por ejemplo
    numero = int(input("Ingresa un número positivo (0 o negativo para salir): "))
    
    if numero <= 0:
        break  # Salir del ciclo si el número es 0 o negativo
    
    suma += numero
    contador += 1

# Mostrar resultados solo si se ingresaron números válidos
if contador > 0:
    promedio = suma / contador
    print("Suma total:", suma)
    print("Promedio:", promedio)
else:
    print("No se ingresaron números positivos.")


#while
""" suma = 0
contador = 0

while True:
    numero = int(input("Ingresa un número positivo (0 o negativo para salir): "))
    
    if numero <= 0:
        break  # Salir del ciclo si el número es 0 o negativo
    
    suma += numero
    contador += 1

# Mostrar resultados solo si se ingresaron números válidos
if contador > 0:
    promedio = suma / contador
    print("Suma total:", suma)
    print("Promedio:", promedio)
else:
    print("No se ingresaron números positivos.") """
