import math
#Taller
#1. Escribir un programa que permita leer la edad y peso de una persona y
#posteriormente imprimirla.
""" edad = input("Introduce tu edad: ")
edad = int(edad) #Convierte la entrada en entero
peso = input("Introduce tu peso: ")
peso = float(peso)
print("Tu edad es:", edad, f"años \nTu peso es: {peso:.2f} Kg") """

#2. Escribir un programa que calcule el área de un triángulo recibiendo como
#entrada el valor de base y altura. Área= base*altura/2
""" base = input("Ingrese la base del triangulo a calcular el area:")
base = float(base)
altura = input("Ingrese la altura del triangulo a calcular el area:")
altura = float(altura)
areaTriangulo = (base*altura)/2
print("El area de un triangulo de base", base, "y altura", altura, f"es: {areaTriangulo:.2f} m^2") """

#3. Escribir un programa que calcule el área de un círculo.
#Area= radio*radio*Pi
""" radio = input("Ingrese el radio en metros del circulo para calcular su area:")
radio = float(radio)
areaCirculo = radio*radio*math.pi
print("El area de un circulo de radio", radio, f"m es: {(areaCirculo):.2f} m^2") """

#4. Hacer un programa que permita ingresar el peso de una persona en kilogramos y
#devolver dicho peso en libras.
""" pesoKg = input("Ingrese su peso en Kg para convertirlo a lb:")
pesoKg = float(pesoKg)
pesolb = pesoKg/2
print("Tu peso de ", pesoKg, f"equivale a {pesolb:.2f}") """

#5. En un supermercado de la ciudad se está aplicando un descuento del 10% sobre
#las compras que hacen los clientes. Diseñar un programa que calcule y escriba el
#descuento en pesos que se hace sobre la compra y el valor total que deberá pagar
#el cliente. Elaborar el algoritmo en pseudocódigo.
""" valor = input("Ingrese valor de la compra para aplicar el descuento del 10%: ")
valor = float(valor)
descuento = valor*0.1
valorPagar = valor-descuento
print(f"Valor Compra: ${valor:.2f} \nDescuento: ${descuento:.2f} \nTotal a pagar: ${valorPagar}") """

#6. Un estudiante tiene 4 notas, se desea calcular la nota definitiva, teniendo en
#cuenta que la primera nota equivale al 30%, la segunda equivale al 30%, la tercera
#al 25% y la última al 15%. Diseñar un programa que permita calcular e imprimir la
#nota definitiva del estudiante. Elaborar el algoritmo en pseudocódigo.
""" nota1 = input("Ingrese la nota 1: ")
nota1 = float(nota1)*0.3
nota2 = input("Ingrese la nota 2: ")
nota2 = float(nota2)*0.3
nota3 = input("Ingrese la nota 3: ")
nota3 = float(nota3)*0.25
nota4 = input("Ingrese la nota 4: ")
nota4 = float(nota4)*0.15
notaFinal = nota1+nota2+nota3+nota4
print(f"Nota 1(30%): {nota1:.1f} \nNota 2(30%): {nota2:.1f} \nNota 3(25%): {nota3:.1f} \nNota 4(15%): {nota4:.1f} \nNota final: {notaFinal:.1f}") """

#7. Construya un programa tal que dados los datos enteros A y B, escriba el resultado
#de la siguiente expresión:
#((A + B)^2)/3
""" datoA = input("Ingrese el valor del entero A: ")
datoA = int(datoA)
datoB = input("Ingrese el valor del entero B: ")
datoB = int(datoB)
resultado = ((datoA + datoB)**2)/3
print(f"(({datoA} + {datoB})^2)/3 = {resultado:.2f}") """

#8. Diseñe un programa que calcule e imprima el número de segundos que hay en un
#determinado número de días.
""" dias = input("Ingrese la cantidad de dias a calcular a segundo: ")
dias = int(dias)
segundos = dias*24*60*60
print(dias, "dias equivalen a", segundos, "segundos") """

#9. Diseñar un programa que lea cuatro valores y calcule e imprima su producto, su
#suma y su promedio.
""" valor1 = input("Ingrese el valor 1: ")
valor1 = float(valor1)
valor2 = input("Ingrese el valor 1: ")
valor2 = float(valor2)
valor3 = input("Ingrese el valor 1: ")
valor3 = float(valor3)
valor4 = input("Ingrese el valor 1: ")
valor4 = float(valor4)
producto = valor1*valor2*valor3*valor4
suma = valor1+valor2+valor3+valor4
promedio = suma/4
print(f"Producto: {producto:.2f} \nSuma: {suma:.2f} \nPromedio: {promedio:.2f}") """

#10. Diseñar un programa que permita calcular e imprimir el salario neto de un
#trabajador conociendo el número de horas trabajadas y el precio de la hora, y
#teniendo en cuenta que se le va a descontar el 8% de lo que se gana.
""" horasTrabajadas = input("Ingrese la cantidad de horas trabajdas: ")
horasTrabajadas = float(horasTrabajadas)
precioHora = input("Ingrese el precio de la hora: ")
precioHora = float(precioHora)
salario = (horasTrabajadas*precioHora)
descuento = salario*0.08
salarioNeto = salario-descuento
print(f"Salario: ${salario:.2f} \nDescuento: ${descuento:.2f} \nSalario neto: ${salarioNeto:.2f}") """