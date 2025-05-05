# Ejercicio 1: Crear un programa que pida al usuario su edad y su peso y lo imprima en pantalla.
""" edad = input("Ingrese su edad: ")
peso = input("Ingrese su peso: ")
edad = int(edad)  # Convertir la edad a un número entero
peso = float(peso)  # Convertir el peso a un número decimal
print("Su edad es:" + str(edad))
print("Su peso es:" + str(peso)) """

# Ejercicio 2: Calcular el area de un triángulo.
""" base = input("Ingrese la base del triangulo en centimetros:")
altura = input("Ingrese la altura del triangulo en centimetros:")
area = (int(base) * int(altura)) / 2
print("El area del triangulo en centimetros cuadrados es: " + str(area))
 """
# Ejercicio 3: Calcular el area de un circulo.
""" import math
radio = input("Ingrese el radio del circulo en centimetros:")
area = math.pi * (int(radio) ** 2)
print("El area del circulo en centimetros cuadrados es: " + str(area)) """
# Ejercicio 4: Convertir de kilos a libras.
""" peso = float(input("Ingrese su peso en kilos:"))
libras = peso * 2.20462
print("Su peso en libras es: " + str(libras)) """

# Ejercicio 5: Supermercado.
""" compra = float(input("Ingrese el total de su compra:"))
descuento = 0.10  # 10% de descuento
descuentoTotal = float(compra * descuento)
total = float(compra - descuentoTotal)
print("El descuento en pesos es: " + str(descuentoTotal))
print("El total de su compra con descuento es: " + str(total)) """

# Ejercicio 6: Calcular el promedio de notas.
""" nota1 = float(input("Ingrese la nota 1:"))
nota2 = float(input("Ingrese la nota 2:"))
nota3 = float(input("Ingrese la nota 3:"))
nota4 = float(input("Ingrese la nota 4:"))
nota1 = nota1 * 0.30
nota2 = nota2 * 0.30
nota3 = nota3 * 0.25
nota4 = nota4 * 0.15
notaFinal = nota1 + nota2 + nota3 + nota4
if notaFinal >= 3.0:
    print("Aprobado")
else:
    print("Reprobado")
print("Su nota final es: " + str(notaFinal)) """

# Ejercicio 7: Dados 2 enteros.
""" num1 = int(input("Ingrese el primer numero entero:"))
num2 = int(input("Ingrese el segundo numero entero:"))
solucion = (num1 + num2)**2 / 3
print("La solucion es: " + str(solucion))
 """
# Ejercicio 8: Conversion de dias a segundos.
""" dias = int(input("Ingrese la cantidad de dias:"))
segundos = dias * 24 * 60 * 60
print("La cantidad de segundos es: " + str(segundos)) """

# Ejercicio 9:Leer 4 valores e imprimir su producto, su suma y su promedio.
""" num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segundo numero:"))
num3 = int(input("Ingrese el tercer numero:"))
num4 = int(input("Ingrese el cuarto numero:"))
suma = num1 + num2 + num3 + num4
producto = num1 * num2 * num3 * num4
promedio = suma / 4
print("La suma es: " + str(suma))
print("El producto es: " + str(producto))
print("El promedio es: " + str(promedio)) """

# Ejercicio 10: Sueldo del trabajador.
""" HorasTrabajadas = float(input("Ingrese la cantidad de horas trabajadas:"))
ValorHora = float(input("Ingrese el valor de la hora:"))
sueldo = HorasTrabajadas * ValorHora
print("Su sueldo sin descontar el 8% es:" + str(sueldo))
sueldoNeto = sueldo - (sueldo * 0.08)
print("El sueldo Neto es: " + str(sueldoNeto)) """

# Ejercicios Parte 2:

# 1. Determinar si un número entero dado por el usuario es par o impar.
""" numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print(f"El número " + str(numero) + " es par.")
else:
    print(f"El número " + str(numero) + " es impar.") """
    
# 2. Determinar si un número dado por el usuario es positivo o negativo.
""" numero = int(input("Ingrese un número: "))
if numero > 0:
    print(f"El número " + str(numero) + " es positivo.")
else:
    print(f"El número " + str(numero) + " es negativo.") """
    
# 3. Determinar en qué estado está el agua en función de su temperatura. Si es negativa el estado será sólido, si es menor que 100 será líquido y si es 100 o mayor que 100 será gas. Pedir al usuario el valor de la temperatura. 
""" temperatura = float(input("Ingrese la temperatura del agua en grados Celsius: "))
if temperatura < 0:
    print("El agua está en estado sólido.")
elif temperatura < 100:
    print("El agua está en estado líquido.")
else:
    print("El agua está en estado gaseoso.") """
    
    # 4. Un año es bisiesto si es divisible por 4 y no es divisible por 100, o es bisiesto si es divisible por 400. Escribir un algoritmo que lea un año y devuelva si es bisiesto o no.
""" año = int(input("Ingrese un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f"El año " + str(año) + " es bisiesto.")
else:
        print(f"El año " + str(año) + " no es bisiesto.") """
        
# 5. Nomina semanal
""" horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
precio_hora = float(input("Ingrese el precio por hora: "))

if horas_trabajadas <= 35:
    salario_bruto = horas_trabajadas * precio_hora
else:
    horas_normales = 35
    horas_extra = horas_trabajadas - 35
    salario_bruto = (horas_normales * precio_hora) + (horas_extra * precio_hora * 1.25)


salario_mensual = salario_bruto * 4


if salario_mensual < 1000:
    impuestos = 0
elif salario_mensual <= 2000:
    impuestos = salario_bruto * 0.20
else:
    impuestos = salario_bruto * 0.30


salario_neto = salario_bruto - impuestos

print(f"\nSalario bruto semanal: {salario_bruto:.2f}€")
print(f"Impuestos semanales: {impuestos:.2f}€")
print(f"Salario neto semanal: {salario_neto:.2f}€") """

