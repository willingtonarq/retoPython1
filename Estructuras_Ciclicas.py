'''
Escribir un algoritmo que calcule la suma de los n primeros números naturales.
Analizar si se puede implementar con los dos tipos de ciclos. El valor de n es dado por
el usuario.

# for
n = int(input("Ingrese un numero: "))
suma = 0

for i in range(1, n + 1, 1):
        suma += i
print(f"La suma de los primeros', {n}, 'numeros es: ', {suma}")


# while
n = int(input("Ingrese un numero: "))
suma = 0
i = 1
while i <= n:
        suma += i
        i += 1
print(f"La suma de los primeros', {n}, 'numeros es: ', {suma}")


Escribir un algoritmo que calcule la suma de los cuadrados de los n primeros números
naturales: 12 + 22 + 32 +… + n2

# for
n = int(input("Ingrese un numero: "))
suma = 0
for i in range(1, n + 1, 1):
        suma += i ** 2 
print(f"La suma de los cuadrados de los primeros', {n}, 'numeros es: ', {suma}")


# while
n = int(input("Ingrese un numero: "))
suma = 0
i = 1
while i <= n:
        suma += i ** 2 
        i += 1
print(f"La suma de los cuadrados de los primeros', {n}, 'numeros es: ', {suma}")


Escribir un algoritmo que calcule la suma de los números enteros de n a m, siendo
m>n, utilizando el algoritmo del ejercicio 1. Los valores de n y m son dados por el
usuario.

# for
n = int(input("Ingrese el primer numero: "))
m = int(input("Ingrese el segundo numero: "))
suma = 0
if n > m:
    print("El primer numero debe ser menor que el segundo")
else:
    for i in range(n, m + 1, 1):
        suma += i
print(f"La suma de los numeros enteros entre', {n}, 'y', {m}, 'es: ', {suma}")

# while
n = int(input("Ingrese el primer numero: "))
m = int(input("Ingrese el segundo numero: "))
suma = 0
i = n
if n > m:
    print("El primer numero debe ser menor que el segundo")
else:
    while i <= m:
        suma += i
        i += 1 
    print(f"La suma de los numeros enteros entre', {n}, 'y', {m}, 'es: ', {suma}")


Implementar un algoritmo que calcule el producto de dos números enteros (n*m)
haciendo sólo sumas.

# for
n = int(input("Ingrese el primer numero: "))
m = int(input("Ingrese el segundo numero: "))
producto = 0
for i in range(1, m + 1, 1):
    producto += n
print(f"El producto de', {n}, 'y', {m}, 'es: ', {producto}")


# while
n = int(input("Ingrese el primer numero: "))
m = int(input("Ingrese el segundo numero: "))
producto = 0
i = 1
while i <= m:
    producto += n
    i += 1
print(f"El producto de', {n}, 'y', {m}, 'es: ', {producto}")



Diseñar un algoritmo que calcule y muestre el promedio de cinco valores de
temperaturas dadas por el usuario.
   
# for
temperaturas = []
for i in range(5):
    temperatura = float(input(f"Ingrese la temperatura {i + 1}: "))
    temperaturas.append(temperatura)
promedio = sum(temperaturas) / len(temperaturas)
print(f"El promedio de las temperaturas es: ', {promedio}")

# while
temperaturas = []
i = 0
while i < 5:
    temperatura = float(input(f"Ingrese la temperatura {i + 1}: "))
    temperaturas.append(temperatura)
    i += 1
promedio = sum(temperaturas) / len(temperaturas)
print(f"El promedio de las temperaturas es: ', {promedio}")


Dada las horas Extras trabajadas de una persona por día en una semana, de lunes a
viernes, y la tarifa de pago. Calcular el valor total a pagar e imprimirlo por pantalla.

# for
horas_extras = []
for i in range(5):
    horas = float(input(f"Ingrese las horas extras trabajadas el dia {i + 1}: "))
    horas_extras.append(horas)
    tarifa = float(6000)
    total = sum(horas_extras) * tarifa
print(f"El valor total a pagar es: ', {total}")

# while
horas_extras = []
i = 0
while i < 5:
    horas = float(input(f"Ingrese las horas extras trabajadas el dia {i + 1}: "))
    horas_extras.append(horas)
    i += 1
    tarifa = float(6000)
    total = sum(horas_extras) * tarifa
print(f"El valor total a pagar es: ', {total}")


Calcular y visualizar la suma y el producto de los números pares comprendidos entre
20 y 400 ambos inclusive

Calcular y visualizar la suma y el producto de los números pares comprendidos entre
20 y 400 ambos inclusive.

# for
suma = 0
producto = 1
for i in range(20, 401, 2):
    suma += i
    producto *= i
print(f"La suma de los numeros pares entre 20 y 400 es: ', {suma}")
print(f"El producto de los numeros pares entre 20 y 400 es: ', {producto}")


# while
suma = 0
producto = 1
i = 20
while i <= 400:
    suma += i
    producto *= i
    i += 2
print(f"La suma de los numeros pares entre 20 y 400 es: ', {suma}")

Realice un algoritmo que permita adivinar un número preestablecido entre 1 y 10,
dando al usuario tres intentos, e informando si adivino o fallo. (ciclos + condicionales)

# for
import random
numero_secreto = random.randint(1, 10)
intentos = 3
for i in range(intentos):
    intento = int(input("Adivina el numero entre 1 y 10: "))
    if intento == numero_secreto:
        print("¡Adivinaste!")
        break
    else:
        print("Intenta de nuevo")
else:
    print(f"Lo siento, el numero era {numero_secreto}")


# while
numero_secreto = random.randint(1, 10)
intentos = 3
i = 0
while i < intentos:
    intento = int(input("Adivina el numero entre 1 y 10: "))
    if intento == numero_secreto:
        print("¡Adivinaste!")
        break
    else:
        print("Intenta de nuevo")
    i += 1
else:
    print(f"Lo siento, el numero era {numero_secreto}")


Realice un algoritmo que solicite sólo números positivos, muestre su suma y promedio,
hasta que el usuario digite 0, o digite un número negativo. (ciclos + condicionales).

#for

suma = 0
contador = 0
for i in range(1, 1000):
    numero = int(input("Ingrese un numero positivo (0 para salir): "))
    if numero <= 0:
        break
    suma += numero
    contador += 1
if contador > 0:
    promedio = suma / contador
    print(f"La suma de los numeros es: {suma}")
    print(f"El promedio de los numeros es: {promedio}")
else:
    print("No se ingreso ningun numero positivo")




#while

suma = 0
contador = 0
while True:
    numero = int(input("Ingrese un numero positivo (0 para salir): "))
    if numero <= 0:
        break
    suma += numero
    contador += 1
if contador > 0:
    promedio = suma / contador
    print(f"La suma de los numeros es: {suma}")
    print(f"El promedio de los numeros es: {promedio}")
else:
    print("No se ingreso ningun numero positivo")


Escriba un algoritmo que genere y muestre la tabla de multiplicar de un número entero
positivo dado por el usuario.


# for
numero = int(input("Ingrese un numero: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

'''

# while
numero = int(input("Ingrese un numero: "))
print(f"Tabla de multiplicar del {numero}:")
i = 1
while i <= 11:
    print(f"{numero} x {i} = {numero * i}")
    i += 1



