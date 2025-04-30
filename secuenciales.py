# 1. Escribir un programa que permita leer la edad y peso de una persona y
# posteriormente imprimirla.
edad=int(input("Ingrese su edad: "))
peso=float(input("Ingrese su peso: "))
print("La edad es: ", edad)
print("El peso es: ", peso)
# 2. Escribir un programa que calcule el área de un triángulo recibiendo como
# entrada el valor de base y altura. Área= base*altura/2
base=float(input("Ingrese la base del triángulo: "))
altura=float(input("Ingrese la altura del triángulo: "))
area=(base*altura)/2
print("El área del triángulo es: ", area)
# 3. Escribir un programa que calcule el área de un círculo.
# Area= radio*radio*Pi
radio=float(input("Ingrese el radio del círculo: "))
pi=3.14159
area=(radio*radio)*pi
print("El área del círculo es: ", area)
# 4. Hacer un programa que permita ingresar el peso de una persona en kilogramos y
# devolver dicho peso en libras.
peso_kg=float(input("Ingrese su peso en kilogramos: "))
peso_libras=peso_kg/2
print("El peso en libras es: ", peso_libras)
# 5. En un supermercado de la ciudad se está aplicando un descuento del 10% sobre
# las compras que hacen los clientes. Diseñar un programa que calcule y escriba el
# descuento en pesos que se hace sobre la compra y el valor total que deberá pagar
# el cliente. Elaborar el algoritmo en pseudocódigo.
compra=float(input("Ingrese el valor de la compra: "))
descuento=compra*0.10
total=compra-descuento
print("El descuento es: ", descuento)
print("El total a pagar es: ", total)
# 6. Un estudiante tiene 4 notas, se desea calcular la nota definitiva, teniendo en
# cuenta que la primera nota equivale al 30%, la segunda equivale al 30%, la tercera
# al 25% y la última al 15%. Diseñar un programa que permita calcular e imprimir la
# nota definitiva del estudiante. Elaborar el algoritmo en pseudocódigo.
nota1=float(input("Ingrese la primera nota: "))
nota2=float(input("Ingrese la segunda nota: "))
nota3=float(input("Ingrese la tercera nota: "))
nota4=float(input("Ingrese la cuarta nota: "))
definitiva=(nota1*0.30)+(nota2*0.30)+(nota3*0.25)+(nota4*0.15)
print("La nota definitiva es: ", definitiva)
# 7. Construya un programa tal que dados los datos enteros A y B, escriba el resultado
# de la siguiente expresión:
# ((A + B)2)/3
A=int(input("Ingrese el valor de A: "))
B=int(input("Ingrese el valor de B: "))
resultado=((A+B)**2)/3
print("El resultado de la expresión es: ", resultado)
# 8. Diseñe un programa que calcule e imprima el número de segundos que hay en un
# determinado número de días.
dias=int(input("Ingrese el número de días: "))
segundos=dias*24*60*60
print("El número de segundos en ", dias, " días es: ", segundos)
# 9. Diseñar un programa que lea cuatro valores y calcule e imprima su producto, su
# suma y su promedio.
valor1=float(input("Ingrese el primer valor: "))
valor2=float(input("Ingrese el segundo valor: "))
valor3=float(input("Ingrese el tercer valor: "))
valor4=float(input("Ingrese el cuarto valor: "))
producto=valor1*valor2*valor3*valor4
suma=valor1+valor2+valor3+valor4
promedio=suma/4
print("El producto es: ", producto)
print("La suma es: ", suma)
print("El promedio es: ", promedio)
# 10. Diseñar un programa que permita calcular e imprimir el salario neto de un
# trabajador conociendo el número de horas trabajadas y el precio de la hora, y
# teniendo en cuenta que se le va a descontar el 8% de lo que se gana.
horas_trabajadas=int(input("Ingrese el número de horas trabajadas: "))
precio_hora=float(input("Ingrese el precio de la hora: "))
salario_bruto=horas_trabajadas*precio_hora
descuento=salario_bruto*0.08
salario_neto=salario_bruto-descuento
print("El salario neto es: ", salario_neto)