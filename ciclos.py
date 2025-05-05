# 1. Escribir un algoritmo que calcule la suma de los n primeros números naturales.
# Analizar si se puede implementar con los dos tipos de ciclos. El valor de n es dado por
# el usuario.
n=int(input("Ingrese un número entero positivo: "))
suma=0
for i in range(1,n+1):
    suma+=i
print("La suma de los",n,"primeros números naturales es:",suma)
# 2. Escribir un algoritmo que calcule la suma de los cuadrados de los n primeros números
# naturales: 12 + 22 + 32 +… + n2
n=int(input("Ingrese un número entero positivo: "))
suma=0
for i in range(1,n+1):
    suma+=i*i
print("La suma de cuadrados de los",n,"primeros números naturales es:",suma)
# 3. Escribir un algoritmo que calcule la suma de los números enteros de n a m, siendo
# m>n, utilizando el algoritmo del ejercicio 1. Los valores de n y m son dados por el
# usuario.
n=int(input("Ingrese un número entero positivo: "))
m=int(input("Ingrese un número entero positivo:: "))
suma=0
for i in range(n,m+1):
    suma+=i
print("La suma de los números enteros de",n,"a",m,"es:",suma)
# 4. Implementar un algoritmo que calcule el producto de dos números enteros (n*m)
# haciendo sólo sumas.
n=int(input("Ingrese un número entero positivo: "))
m=int(input("Ingrese un número entero positivo: "))
suma=0
for i in range(m):
    suma+=n
print("El producto de",n,"y",m,"es:",suma)
# 5. Diseñar un algoritmo que calcule y muestre el promedio de cinco valores de
# temperaturas dadas por el usuario.
for i in range(5):
    print("Ingrese la temperatura",i+1,":")
    if i==0:
        t1=float(input())
    elif i==1:
        t2=float(input())
    elif i==2:
        t3=float(input())
    elif i==3:
        t4=float(input())
    else:
        t5=float(input())
suma=t1+t2+t3+t4+t5
promedio=suma/5
print("La suma de las temperaturas es:",suma)
print("El promedio de las temperaturas es:",promedio)
# 6. Dada las horas Extras trabajadas de una persona por día en una semana, de lunes a
# viernes, y la tarifa de pago. Calcular el valor total a pagar e imprimirlo por pantalla.
tarifa=float(input("Ingrese la tarifa de pago por hora extra: "))
for i in range(5):
    print("Ingrese las horas extras trabajadas el día",i+1,":")
    if i==0:
        h1=float(input())
    elif i==1:
        h2=float(input())
    elif i==2:
        h3=float(input())
    elif i==3:
        h4=float(input())
    else:
        h5=float(input())
horas=h1+h2+h3+h4+h5
total=tarifa*horas
print("El total a pagar es:",total)
# 7. Calcular y visualizar la suma y el producto de los números pares comprendidos entre
# 20 y 400 ambos inclusive.
suma=0
producto=1
for i in range(20,401):
    if i%2==0:
        suma+=i
        producto*=i
print("La suma de los números pares entre 20 y 400 es:",suma)
print("El producto de los números pares entre 20 y 400 es:",producto)
# 8. Realice un algoritmo que permita adivinar un número preestablecido entre 1 y 10,
# dando al usuario tres intentos, e informando si adivino o fallo. (ciclos + condicionales)
numero_preestablecido=5
intentos=3
for i in range(intentos):
    print("Adivina el número entre 1 y 10:")
    numero_usuario=int(input())
    if numero_usuario==numero_preestablecido:
        print("¡Adivinaste! El número es:",numero_preestablecido)
        break
    else:
        print("Fallaste. Te quedan",intentos-i-1,"intentos.")
# 9. Realice un algoritmo que solicite sólo números positivos, muestre su suma y promedio,
# hasta que el usuario digite 0, o digite un número negativo. (ciclos + condicionales).
suma=0
contador=0
while True:
    print("Ingrese un número positivo (0 para salir):")
    numero_usuario=int(input())
    if numero_usuario<0:
        print("Número negativo. Saliendo...")
        break
    elif numero_usuario==0:
        print("Número cero. Saliendo...")
        break
    else:
        suma+=numero_usuario
        contador+=1
promedio=suma/contador
print("La suma de los números positivos es:",suma)
print("El promedio de los números positivos es:",promedio)
# 10. Escriba un algoritmo que genere y muestre la tabla de multiplicar de un número entero
# positivo dado por el usuario.
n=int(input("Ingrese un número entero positivo: "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)