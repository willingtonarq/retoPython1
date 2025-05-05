git 

"""
Este programa permite leer la edad y peso de una persona y
posteriormente imprimirla.
"""
# Leer la edad y el peso de la persona
edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso (en kg): "))

# Imprimir la edad y el peso
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")


"""2. Escribir un programa que calcule el área de un triángulo recibiendo como
entrada el valor de base y altura. Área= base*altura/2"""
# Leer la base y la altura del triángddulo
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
# Calcular el área del triángulo
area = (base * altura) / 2
# Imprimir el área del triángulo
print(f"Área del triángulo: {area} unidades cuadradas")



"""Escribir un programa que calcule el área de un círculo.
Area= radio*radio*Pi"""

# Importar la constante Pi de la biblioteca math
import math
# Leer el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))
# Calcular el área del círculo
area_circulo = math.pi * (radio ** 2)
# Imprimir el área del círculo
print(f"Área del círculo: {area_circulo} unidades cuadradas")




"""Hacer un programa que permita ingresar el peso de una persona en kilogramos y
devolver dicho peso en libras."""
peso = float(input("Ingrese su peso (en kg): "))
peso_libras = peso * 2.20462
print(f"Su peso en libras es: {peso_libras} lbs")


"""En un supermercado de la ciudad se está aplicando un descuento del 10% sobre
las compras que hacen los clientes. Diseñar un programa que calcule y escriba el
descuento en pesos que se hace sobre la compra y el valor total que deberá pagar
el cliente."""
# Leer el monto de la compra
monto_compra = float(input("Ingrese el monto de la compra: "))
# Calcular el descuento
descuento = monto_compra * 0.10
# Calcular el monto total a pagar
monto_total = monto_compra - descuento
# Imprimir el descuento y el monto total a pagar
print(f"Descuento: {descuento} pesos")
print(f"Monto total a pagar: {monto_total} pesos")




"""6. Un estudiante tiene 4 notas, se desea calcular la nota definitiva, teniendo en
cuenta que la primera nota equivale al 30%, la segunda equivale al 30%, la tercera
al 25% y la última al 15%. Diseñar un programa que permita calcular e imprimir la
nota definitiva del estudiante."""

# Leer las notas del estudiante
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
nota4 = float(input("Ingrese la cuarta nota: "))
# Calcular la nota definitiva
def calcular_nota_definitiva(nota1, nota2, nota3, nota4):
    return (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.25) + (nota4 * 0.15)

print(f"Nota definitiva: {calcular_nota_definitiva(nota1, nota2, nota3, nota4)}")


"""Construya un programa tal que dados los datos enteros A y B, escriba el resultado
de la siguiente expresión:
((A + B)^2)/2"""


# Leer los valores de A y B
a =float(input("Ingrese el valor de A: "))
b = float(input("Ingrese el valor de B: "))

def calcular_expresion(a, b):
    return((a + b) ** 2) / 2
# Imprimir el resultado de la expresión
print(f"Resultado de la expresión: {calcular_expresion(a, b)}")





"""Diseñe  un programa que calcule e imprima el número de segundos que hay en un
    determinado número de días."""

# Leer el número de días
dias=float(input("ingrese numero de dias "))

def calcular_dias(dias):
    return (dias)* 86400
    
    print (f"nuemero de dias= {dias} ,los segundos son= {calcular_dias(dias)}")




""" Diseñar un programa que lea cuatro valores y calcule e imprima su producto, su
suma y su promedio."""
valor1 = float(input("Ingrese el primer valor: "))
valor2 = float(input("Ingrese el segundo valor: "))
valor3 = float(input("Ingrese el tercer valor: "))
valor4 = float(input("Ingrese el cuarto valor: "))

producto = valor1 * valor2 * valor3 * valor4
suma = valor1 + valor2 + valor3 + valor4
promedio = suma / 4




print(f"Producto: {producto} SUMA; {suma} promedio: {promedio}")  


"""10. Diseñar un programa que permita calcular e imprimir el salario neto de un
trabajador conociendo el número de horas trabajadas y el precio de la hora, y
teniendo en cuenta que se le va a descontar el 8% de lo que se gana."""


# Leer el número de horas trabajadas y el precio de la hora
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
precio_hora = float(input("Ingrese el precio de la hora: "))
# Calcular el salario bruto
salario_bruto = horas_trabajadas * precio_hora
# Calcular el descuento
descuento = salario_bruto * 0.08
# Calcular el salario neto
salario_neto = salario_bruto - descuento
# Imprimir el salario neto
print(f"Salario neto: {salario_neto} pesos")


"""Determinar si un número entero dado por el usuario es par o impar"""

# Leer un número entero
numero = int(input("Ingrese un número entero: "))
# Verificar si el número es par o impar
if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")



"""Diseñar un programa que lea un número entero y determine si es positivo, negativo"""
# o cero.
# Leer un número entero
numero = int(input("Ingrese un número entero: "))
# Verificar si el número es positivo, negativo o cero
if numero > 0:
    print(f"{numero} es un número positivo.")
elif numero < 0:
    print(f"{numero} es un número negativo.")
else:
    print(f"{numero} es cero.")     
    






