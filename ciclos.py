"""1. Escribir un algoritmo que calcule la suma de los n primeros números naturales.
Analizar si se puede implementar con los dos tipos de ciclos. El valor de n es dado por
el usuario."""

# Leer el valor de n
n = int(input("Ingrese el valor de n: "))


suma = 0
for i in range (1,n+1,1):
    suma += i
print(f"La suma de los {n} primeros números naturales es: {suma}")



# Usando while
suma = 0
i = 1
while i <= n:
    suma += i
    i += 1
print(f"La suma de los {n} primeros números naturales es: {suma}")

"""Escribir un algoritmo que calcule la suma de los cuadrados de los n primeros números
naturales: 12 + 22 + 32 +… + n2"""

# Leer el valor de n
n = int(input("Ingrese el valor de n: "))
suma_cuadrados = 0
for i in range(1, n + 1):
    suma_cuadrados += i ** 2
print(f"La suma de los cuadrados de los {n} primeros números naturales es: {suma_cuadrados}")

# Usando while
suma_cuadrados = 0
i = 1
while i <= n:
    suma_cuadrados += i ** 2
    i += 1
print(f"La suma de los cuadrados de los {n} primeros números naturales es: {suma_cuadrados}")


""" Escribir un algoritmo que calcule la suma de los números enteros de n a m, siendo
m>n, utilizando el algoritmo del ejercicio 1. Los valores de n y m son dados por el
usuario."""
# Leer los valores de n y m
n = int(input("Ingrese el valor de n: "))
m = int(input("Ingrese el valor de m: "))
# Verificar que m > n
if m > n:
    suma = 0
    for i in range(n, m + 1):
        suma += i
    print(f"La suma de los números enteros de {n} a {m} es: {suma}")
else:
    print("Error: m debe ser mayor que n.")
# Usando while
suma = 0
i = n
while i <= m:
    suma += i
    i += 1
print(f"La suma de los números enteros de {n} a {m} es: {suma}")


""". Escribir un algoritmo que calcule la suma de los números enteros de n a m, siendo
m>n, utilizando el algoritmo del ejercicio 1. Los valores de n y m son dados por el
usuario."""
# Leer los valores de n y m
n = int(input("Ingrese el valor de n: "))
m = int(input("Ingrese el valor de m: "))
# Verificar que m > n
if m > n:
    suma = 0
    for i in range(n, m + 1):
        suma += i
    print(f"La suma de los números enteros de {n} a {m} es: {suma}")
else:
    print("Error: m debe ser mayor que n.")
# Usando while
suma = 0
i = n
while i <= m:
    suma += i
    i += 1
print(f"La suma de los números enteros de {n} a {m} es: {suma}")    


"""5. Diseñar un algoritmo que calcule y muestre el promedio de cinco valores de
temperaturas dadas por el usuario."""
# Leer las temperaturas
temperaturas = []
for i in range(5):
    temperatura = float(input(f"Ingrese la temperatura {i + 1}: "))
    temperaturas.append(temperatura)
# Calcular el promedio
promedio = sum(temperaturas) / len(temperaturas)
print(f"El promedio de las temperaturas es: {promedio}")

#` Usando while
temperaturas = []
i = 0
while i < 5:
    temperatura = float(input(f"Ingrese la temperatura {i + 1}: "))
    temperaturas.append(temperatura)
    i += 1
    # Calcular el promedio
    promedio = sum(temperaturas) / len(temperaturas)
    print(f"El promedio de las temperaturas es: {promedio}")


"""6. Dada las horas Extras trabajadas de una persona por día en una semana, de lunes a
viernes, y la tarifa de pago. Calcular el valor total a pagar e imprimirlo por pantalla."""
# Leer las horas extras trabajadas y la tarifa de pago
horas_extras = []
tarifa_pago = float(input("Ingrese la tarifa de pago por hora extra: "))

for i in range(5):
    horas_extra = float(input(f"Ingrese las horas extras trabajadas el día {i + 1}: "))
    horas_extras.append(horas_extra)
# Calcular el valor total a pagar
valor_total = sum(horas_extras) * tarifa_pago
print(f"El valor total a pagar por las horas extras trabajadas es: {valor_total}")
# Usando while
horas_extras = []
i = 0
while i < 5:
    horas_extra = float(input(f"Ingrese las horas extras trabajadas el día {i + 1}: "))
    horas_extras.append(horas_extra)
    i += 1
# Calcular el valor total a pagar
valor_total = sum(horas_extras) * tarifa_pago
print(f"El valor total a pagar por las horas extras trabajadas es: {valor_total}")


"""Calcular y visualizar la suma y el producto de los números pares comprendidos entre
20 y 400 ambos inclusive.""" 

# Inicializar variables
suma = 0
producto = 1
# Calcular la suma y el producto de los números pares
for i in range(20, 401):
    if i % 2 == 0:
        suma += i
        producto *= i
# Imprimir los resultados
print(f"La suma de los números pares entre 20 y 400 es: {suma}")    
print(f"El producto de los números pares entre 20 y 400 es: {producto}")

# Usando while
suma = 0
producto = 1
i = 20
while i <= 400:
    if i % 2 == 0:
        suma += i
        producto *= i
    i += 1
# Imprimir los resultados
print(f"La suma de los números pares entre 20 y 400 es: {suma}")
print(f"El producto de los números pares entre 20 y 400 es: {producto}")



"""Realice un algoritmo que permita adivinar un número preestablecido entre 1 y 10,
dando al usuario tres intentos, e informando si adivino o fallo. (ciclos + condicionales)"""
# Número preestablecido
numero_preestablecido = 7
# Inicializar intentos
intentos = 3
# Bucle para permitir al usuario adivinar el número
while intentos > 0:
    # Leer el número ingresado por el usuario
    numero_usuario = int(input("Adivina el número (entre 1 y 10): "))
    # Verificar si el número es correcto
    if numero_usuario == numero_preestablecido:
        print("¡Adivinaste!")
        break
    else:
        intentos -= 1
        print(f"Fallaste. Te quedan {intentos} intentos.")
# Verificar si se agotaron los intentos
if intentos == 0:
    print(f"Lo siento, el número era {numero_preestablecido}.")

    # Usando for
numero_preestablecido = 7
# Bucle para permitir al usuario adivinar el número
for intento in range(3):
    # Leer el número ingresado por el usuario
    numero_usuario = int(input("Adivina el número (entre 1 y 10): "))
    # Verificar si el número es correcto
    if numero_usuario == numero_preestablecido:
        print("¡Adivinaste!")
        break
    else:
        print(f"Fallaste. Te quedan {2 - intento} intentos.")
# Verificar si se agotaron los intentos
if intento == 2:
    print(f"Lo siento, el número era {numero_preestablecido}.")


"""9. Realice un algoritmo que solicite sólo números positivos, muestre su suma y promedio,
hasta que el usuario digite 0, o digite un número negativo. (ciclos + condicionales)."""
# Inicializar variables
suma = 0
contador = 0
# Bucle para solicitar números positivos
while True:
    numero = int(input("Ingrese un número positivo (0 para salir): "))
    # Verificar si el número es 0 o negativo
    if numero < 0:
        break
    # Sumar el número y aumentar el contador
    suma += numero
    contador += 1
# Calcular el promedio
if contador > 0:
    promedio = suma / contador
    print(f"La suma de los números positivos es: {suma}")
    print(f"El promedio de los números positivos es: {promedio}")
else:
    print("No se ingresaron números positivos.")
# Usando for