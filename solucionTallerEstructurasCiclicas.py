#Para los siguientes ejercicios, después de hallar la solución al problema, desarrolle su
#correspondiente programa, utilizando estructuras cíclicas vistas en clase.

#1. Escribir un algoritmo que calcule la suma de los n primeros números naturales.
#Analizar si se puede implementar con los dos tipos de ciclos. El valor de n es dado por
#el usuario.
""" nNumeros = input("Ingrese la cantidad de primeros numeros a sumar: ")
nNumeros = int(nNumeros)
sumaNumeros = 0
#ciclo for
for i in range(1,nNumeros+1):
    sumaNumeros += i
print(f"las suma de los {nNumeros} primeros numeros naturales es: {sumaNumeros}")

#ciclo while
contador = 1
while contador < nNumeros+1:
    print(contador)
    sumaNumeros += contador
    contador += 1 
    
print(f"las suma de los {nNumeros} primeros numeros naturales es: {sumaNumeros}")"""
#2. Escribir un algoritmo que calcule la suma de los cuadrados de los n primeros números
#naturales: 12 + 22 + 32 +… + n2.
""" nNumeros = input("Ingrese la cantidad de primeros numeros naturales al cuadrado a sumar: ")
nNumeros = int(nNumeros)
sumaNumeros = 0
for i in range(1,nNumeros+1):
    sumaNumeros += i**2
print(f"las suma de los {nNumeros} primeros numeros naturales al cuadrado es: {sumaNumeros}") """

#3. Escribir un algoritmo que calcule la suma de los números enteros de n a m, siendo
#m>n, utilizando el algoritmo del ejercicio 1. Los valores de n y m son dados por el
#usuario.
""" nNumeros = input("Ingrese el valor de n: ")
nNumeros = int(nNumeros)
mNumeros = input("Ingrese el valor de m: ")
mNumeros = int(mNumeros)
sumaNumeros = 0

if mNumeros>nNumeros:
    #ciclo for
    for i in range(nNumeros,mNumeros+1):
        sumaNumeros += i
    
    #ciclo while
    contador = nNumeros
    while contador < mNumeros+1:
        sumaNumeros += contador
        contador += 1 
    
    print(f"las suma de {nNumeros} hasta {mNumeros} es: {sumaNumeros}")
    
else:
    print(f"m = {mNumeros} es menor que n = {nNumeros}")   
 """

#4. Implementar un algoritmo que calcule el producto de dos números enteros (n*m)
#haciendo sólo sumas.
""" numero1 = input("Ingrese el valor del primer numero: ")
numero1 = int(numero1)
numero2 = input("Ingrese el valor del segundo numero: ")
numero2 = int(numero2)
sumaNumeros = numero1
print(f"{sumaNumeros} + {numero1} = {sumaNumeros}" )
for i in range(numero1,numero2+1):
    sumaNumeros += numero1
    print(f"{sumaNumeros} + {numero1} = {sumaNumeros}" ) """
    
#5. Diseñar un algoritmo que calcule y muestre el promedio de cinco valores de
#temperaturas dadas por el usuario.
""" valorTemp = 0
sumaTemp = 0
for i in range(5):
    valorTemp = input(f"Ingres el valor de la temperatura {i+1}: ")
    valorTemp = float(valorTemp)
    sumaTemp += valorTemp
print(sumaTemp)
sumaTemp/=5
print(f"El promedio de las 5 temperatras es: {sumaTemp}°") """

#6. Dada las horas Extras trabajadas de una persona por día en una semana, de lunes a
#viernes, y la tarifa de pago. Calcular el valor total a pagar e imprimirlo por pantalla.
""" valorHorasExtras = input("Ingrese el valor de las horas extras: ")
valorHorasExtras = float(valorHorasExtras)
horasExtrasTotales = 0

for i in range(5):
    if i == 0:
        dia = "Lunes"
    elif i == 1:
        dia = "Martes"
    elif i == 2:
        dia = "Miercoles"
    elif i == 3:
        dia = "Jueves"
    else:
        dia = "Viernes"

    horasExtras = input(f"Ingrese la cantidad de horas extras trabjadas en {dia}: ")
    horasExtras = int(horasExtras)
    horasExtrasTotales += horasExtras

print(f"El total a pagar por {horasExtrasTotales} horas extras semanales es: ${horasExtrasTotales*valorHorasExtras}")
 """

#7. Calcular y visualizar la suma y el producto de los números pares comprendidos entre
#20 y 400 ambos inclusive.
""" sumaTotal=0
productoTotal=1
for i in range(20,400+1,2):
    print(f"{sumaTotal} + {i} = {sumaTotal+i}")
    sumaTotal+=i
    print(f"{productoTotal} + {i} = {sumaTotal*i}")
    productoTotal*=i

print(f"Suma Total: {sumaTotal} \nProducto total: {productoTotal}") """

#8. Realice un algoritmo que permita adivinar un número preestablecido entre 1 y 10,
#dando al usuario tres intentos, e informando si adivino o fallo. (ciclos + condicionales)
""" numeroOculto = 2
intentos = 3

while intentos > 0:
    numero = input("Ingresa un numero y trata de adivinar cual es el coulto entre 1 y 10: ")
    numero = int(numero)
    if numero > 0 and numero < 11:
        if numero > numeroOculto:
            print("El numero oculto es menor")
        elif numero < numeroOculto:
            print("EL numero oculto es mayor")
        else:
            print("adivinaste el numero :D")
            break
        intentos -= 1
        print(f"Intentos restante {intentos}")
    else:
        print("EL numero ingresado esta fuera del rango")

if intentos == 0:
    print("Agotaste los intentos :(") """

#9. Realice un algoritmo que solicite sólo números positivos, muestre su suma y promedio,
#hasta que el usuario digite 0, o digite un número negativo. (ciclos + condicionales).
""" suma = 0
promedio = 0
numero = 1
contador = 0
while numero > 0:
    numero = input("Ingrese 0 un numero negativo pa salir \n" \
    "O ingrese un positivo para sumar con los demas y mostar promedio: ")
    numero = int(numero)
    if numero > 0:
        suma += numero
        contador +=1

if contador == 0:
    print("No Hay valores para operar")
else:
    print(f"Suma: {suma} \nPromedio: {suma/contador}") """

#10. Escriba un algoritmo que genere y muestre la tabla de multiplicar de un número entero
#positivo dado por el usuario.
numero = 0
while numero < 1:
    numero = input("Ingrese un numero positivo para sacar su tabla de multiplicacion: ")
    numero = int(numero)
    if numero < 1:
        print("El numero ingresado es neagtivo o 0, ingrese un numero positivo porfavor")

for i in range(11):
    print(f"{numero} * {i} = {numero*i}")