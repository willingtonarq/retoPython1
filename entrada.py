import math
#Escribir un programa que permita leer la edad y peso de una persona y
#posteriormente imprimirla.

'''
edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso: "))
print("La edad es:", edad)
print("El peso es:", peso)

#Escribir un programa que calcule el área de un triángulo recibiendo como
#entrada el valor de base y altura. Área= base*altura/2
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))  
print("El área del triángulo es:", base * altura / 2)


#Escribir un programa que calcule el área de un círculo.
# Area= radio*radio*Pi


radio = float(input("Ingrese el radio del círculo: "))
pi = 3.1416
area = pi * radio ** 2
print("El área del círculo es:", area)

#Hacer un programa que permita ingresar el peso de una persona en kilogramos y
#devolver dicho peso en libras.

peso_kg = float(input("Ingrese su peso en kilogramos: "))
peso_lb = peso_kg * 2.20462
print("Su peso en libras es:", peso_lb)


En un supermercado de la ciudad se está aplicando un descuento del 10% sobre
las compras que hacen los clientes. Diseñar un programa que calcule y escriba el
descuento en pesos que se hace sobre la compra y el valor total que deberá pagar
el cliente.

compra = float(input("Ingrese el valor de su compra: "))
descuento = compra * 0.10
total = compra - descuento
print("El descuento es:", descuento)
print("El total a pagar es:", total)


Un estudiante tiene 4 notas, se desea calcular la nota definitiva, teniendo en
cuenta que la primera nota equivale al 30%, la segunda equivale al 30%, la tercera
al 25% y la última al 15%. Diseñar un programa que permita calcular e imprimir la
nota definitiva del estudiante.

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
nota4 = float(input("Ingrese la cuarta nota: "))

promedio1 = nota1 * 0.30
promedio2 = nota2 * 0.30
promedio3 = nota3 * 0.25
promedio4 = nota4 * 0.15
total = promedio1+ promedio2+ promedio3+ promedio4

print("nota definitiva:" , total)

Construya un programa tal que dados los datos enteros A y B, escriba el resultado
de la siguiente expresión:
(A + B)**2 /3

A = float(input("Ingrese el numero entero A: "))
B = float(input("Ingrese el numero entro B: "))
oprecion = (A +B) **2 / 3

print("El calculo es: ", oprecion)


Diseñe un programa que calcule e imprima el número de segundos que hay en un
determinado número de días.


dias = float(input("Ingrese el numero de dias: "))
calculo = 60 * 60 * 24 * dias
print("Numero de segundos: ", calculo)

Diseñar un programa que lea cuatro valores y calcule e imprima su producto, su
suma y su promedio.

numero1 = float(input("ingrese el numero 1: "))
numero2 = float(input("Ingrese el numero 2: "))
numero3 = float(input("Ingrese el numero 3: "))
numero4 = float(input("ingrese el numero 4: "))

Producto = numero1 * numero2 * numero3 * numero4
Suma = numero1 + numero2 + numero3 + numero4
Promedio = (numero1 + numero2 + numero3 + numero4) /4

print("El producto es: ", Producto, "La suma es: ", Suma , "El promedio es: ",Promedio)
'''
horas_trabajadas =float(input("Ingrese el numero de horas trabajadas: "))
hora = 6189
total_horas = horas_trabajadas * hora
Porcentaje = total_horas * 0.08

print("Salario neto: ",total_horas - Porcentaje)


      