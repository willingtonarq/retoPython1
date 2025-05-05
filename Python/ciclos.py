# . Escribir un algoritmo que calcule la suma de los n primeros números naturales.
# Analizar si se puede implementar con los dos tipos de ciclos. El valor de n es dado por
# el usuario
n = int(input("Ingrese un número natural: "))
suma = 0
for i in range(1, n + 1):
    suma += i
print("La suma de los primeros", n, "números naturales es:", suma)
# Escribir un algoritmo que calcule la suma de los cuadrados de los n primeros números
# naturales: 12 + 22 + 32 +… + n2
n = int(input("Ingrese un número natural: "))
suma = 0
for i in range(1, n + 1):
    suma += i ** 2
print("La suma de los cuadrados de los primeros", n, "números naturales es:", suma)

# 3. Escribir un algoritmo que calcule la suma de los números enteros de n a m, siendo
# m>n, utilizando el algoritmo del ejercicio 1. Los valores de n y m son dados por el
# usuario.
n = int(input("Ingrese el valor de n: "))
m = int(input("Ingrese el valor de m: "))
suma = 0
for i in range(n, m + 1):
    suma += i       
print("La suma de los números enteros de", n, "a", m, "es:", suma)
# 4. Implementar un algoritmo que calcule el producto de dos números enteros (n*m)
# haciendo sólo sumas.
n = int(input("Ingrese el primer número: "))
m = int(input("Ingrese el segundo número: "))
suma = 0
for i in range(m):
    suma += n
print("El producto de", n, "y", m, "es:", suma)
    
# 5. Diseñar un algoritmo que calcule y muestre el promedio de cinco valores de
# temperaturas dadas por el usuario.
temperaturas = []
for i in range(5):
    temperatura = float(input("Ingrese la temperatura: "))
    temperaturas.append(temperatura)
promedio = sum(temperaturas) / len(temperaturas)
print("El promedio de las temperaturas es:", promedio)
# 6. 4a
# viernes, y la tarifa de pago. Calcular el valor total a pagar e imprimirlo por pantalla.
horas_extras = []
tarifa = float(input("Ingrese la tarifa de pago por hora extra: "))
for i in range(5):
    horas = float(input(f"Ingrese las horas extras trabajadas el día {i + 1}: "))
    horas_extras.append(horas)
total_pago = sum(horas_extras) * tarifa
print("El valor total a pagar por las horas extras es:", total_pago)
# 7. Calcular y visualizar 
# sula suma y el producto de los números pares comprendidos entre
# 20 y 400 ambos inclusive.
suma = 0
producto = 1
for i in range(20, 401):
    if i % 2 == 0:
        suma += i
        producto *= i
print("La suma de los números pares entre 20 y 400 es:", suma)
print("El producto de los números pares entre 20 y 400 es:", producto)
# 8. Realice un algoritmo que permita adivinar un número preestablecido entre 1 y 10,
# dando al usuario tres intentos, e informando si adivino o fallo. (ciclos + condicionales)
numero_secreto = 7
intentos = 3
for i in range(intentos):
    adivina = int(input("Adivina el número entre 1 y 10: "))
    if adivina == numero_secreto:
        print("¡Adivinaste!")
        break
    else:
        print("Fallaste. Te quedan", intentos - i - 1, "intentos.")

# 9. Realice un algoritmo que solicite sólo números positivos, muestre su suma y promedio,
# hasta que el usuario digite 0, o digite un número negativo. (ciclos + condicionales).
suma = 0
contador = 0
while True:
    numero = int(input("Ingrese un número positivo (0 para salir): "))
    if numero < 0:
        print("Número negativo. Saliendo...")
        break
    elif numero == 0:
        print("Saliendo...")
        break
    else:
        suma += numero
        contador += 1
if contador > 0:
    promedio = suma / contador
    print("La suma de los números positivos es:", suma)
    print("El promedio de los números positivos es:", promedio)
# 10. Escriba un algoritmo que genere y muestre la tabla de multiplicar de un número entero
# positivo dado por el usuario
n = int(input("Ingrese un número entero positivo: "))
for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")

