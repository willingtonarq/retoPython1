# .
# 1. Escribir un algoritmo que calcule la suma de los n primeros números naturales.
# Analizar si se puede implementar con los dos tipos de ciclos. El valor de n es dado por
# el usuario.

n = int(input("Ingrese un número natural: "))
for i in range(1, n + 1):
    suma = 0
    suma += i
print("La suma de los primeros", n, "números naturales es:", suma)

# 2. Escribir un algoritmo que calcule la suma de los cuadrados de los n primeros números
# naturales: 12 + 22 + 32 +… + n2
# .
n= int(input("Ingrese un número natural: "))
for i in range(1, n + 1):
    suma = 0
    suma += i*i
print("La suma de los cuadrados de los primeros", n, "números naturales es:", suma)

# 3. Escribir un algoritmo que calcule la suma de los números enteros de n a m, siendo
# m>n, utilizando el algoritmo del ejercicio 1. Los valores de n y m son dados por el
# usuario.

n = int(input("Ingrese un número entero: "))
m = int(input("Ingrese otro número entero mayor que el primero: "))

if m > n:
    suma = 0
    for i in range(n, m + 1):
        suma += i
    print("La suma de los números enteros de", n, "a", m, "es:", suma)
    

# 4. Implementar un algoritmo que calcule el producto de dos números enteros (n*m)
# haciendo sólo sumas.
n= int(input("Ingrese un número entero 1: "))
m= int(input("Ingrese un número entero 2: "))

while m > 0:
    suma = 0
    for i in range(1, m + 1):
        suma += n
    print("El producto de", n, "y", m, "es:", suma)
    break

# 5. Diseñar un algoritmo que calcule y muestre el promedio de cinco valores de
# temperaturas dadas por el usuario.
for i in range(5):
    temperatura = float(input("Ingrese la temperatura: "))
    suma = 0
    suma += temperatura
    promedio = suma / 5
print("El promedio de las temperaturas es:", promedio)

# 6. Dada las horas Extras trabajadas de una persona por día en una semana, de lunes a
# viernes, y la tarifa de pago. Calcular el valor total a pagar e imprimirlo por pantalla.

tarifa_pago = float(input("Ingrese la tarifa de pago por hora extra: "))
for i in range(5):
    horas_extras = float(input("Ingrese las horas extras trabajadas el día " + str(i + 1) + ": "))
    total_pago = 0
    total_pago += horas_extras * tarifa_pago
print("El valor total a pagar por las horas extras trabajadas es:", total_pago)

# 7. Calcular y visualizar la suma y el producto de los números pares comprendidos entre
# 20 y 400 ambos inclusive.
for i in range(20, 401):
    if i % 2 == 0:
        suma = 0
        suma += i
        producto = 1
        producto *= i
print("La suma de los números pares entre 20 y 400 es:", suma)
print("El producto de los números pares entre 20 y 400 es:", producto)

# 8. Realice un algoritmo que permita adivinar un número preestablecido entre 1 y 10,
# dando al usuario tres intentos, e informando si adivino o fallo. (ciclos + condicionales)
numero_preestablecido = 7
intentos = 3
for i in range(intentos):
    numero_adivinado = int(input("Adivina el número entre 1 y 10: "))
    if numero_adivinado == numero_preestablecido:
        print("¡Adivinaste! El número es:", numero_preestablecido)
        break
    else:
        print("Fallaste. Te quedan", intentos - i - 1, "intentos.")
else:
    print("Lo siento, no adivinaste el número. El número era:", numero_preestablecido)

# 9. Realice un algoritmo que solicite sólo números positivos, muestre su suma y promedio,
# hasta que el usuario digite 0, o digite un número negativo. (ciclos + condicionales).
numero = 0
suma = 0
for i in range(1, 100):
    numero = int(input("Ingrese un número positivo (0 para salir): "))
    if numero < 0:
        print("Número negativo ingresado. Saliendo...")
        break
    elif numero == 0:
        print("Saliendo...")
        break
    else:
        suma += numero
        promedio = suma / (i + 1)
        print("La suma de los números positivos ingresados es:", suma)
        print("El promedio de los números positivos ingresados es:", promedio)

# 10. Escriba un algoritmo que genere y muestre la tabla de multiplicar de un número entero
# positivo dado por el usuario.
n= int(input("Ingrese un número entero positivo: "))
for i in range(1, 11):
    resultado = n * i
    print(n, "x", i, "=", resultado)