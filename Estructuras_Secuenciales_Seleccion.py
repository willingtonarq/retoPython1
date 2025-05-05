#primer ejemplo de python 
print("Hello world")


# Ejercicio 1 (edad y peso)
edad = int(input("¿Cuál es tu edad?"))
peso = float(input("¿Cuál es tu peso?"))

print(f"\nLa edad es: {edad} años")
print(f"El peso es:  {peso} kg")


# Ejercicio 2 (area triangulo)= Area = (base * altura) / 2
base = float(input("¿Cuál es la base del triángulo?"))
altura = float(input("¿Cuál es la altura del triángulo?"))
area = (base * altura) / 2
print(f"\nEl área del triángulo es: {area} cm²")


# Ejercicio 3 (area circulo)= Area = pi * radio^2
radio = float(input("por favor, introduce el radio del círculo: "))
import math # Importar la librería math para usar pi
area_circulo = math.pi * (radio ** 2)
print(f"\nEl área del círculo es: {area_circulo} cm²")


# Ejercicio 4 (peso en kg a lb)= 1 kg = 2.20462 lb
peso_kg = float(input("¿Cuál es tu peso en kg?"))
peso_lb = peso_kg * 2.20462 
print(f"\nTu peso en libras es: {peso_lb} lb")


# Ejercicio 5 (supermercado descuesto 10%)= precio = precio - (precio * 0.10)
compra  = float(input("¿Cuál es el precio del producto?"))
descuento =  compra * 0.10
precio_con_descuento = compra - descuento
print(f"\nEl precio con descuento es: {descuento} $")
print(f"Total pago: {precio_con_descuento} $")


# Ejercicio 6 (calcular 4 notas) primera nota =0.3, segunda =0.3; tercera =0.25; cuarta =0.15
nota1 = float(input("¿Cuál es la primera nota?"))
nota2 = float(input("¿Cuál es la segunda nota?"))           
nota3 = float(input("¿Cuál es la tercera nota?"))
nota4 = float(input("¿Cuál es la cuarta nota?"))
promedio = (nota1 * 0.3) + (nota2 * 0.3) + (nota3 * 0.25) + (nota4 * 0.15)
print(f"\nEl promedio es: {promedio}")  


# Ejercicio 7 (datos A y B) resultado expresion = (A + B)**2 / 3
A = int(input("¿Cuál es el valor de A?"))
B = int(input("¿Cuál es el valor de B?"))
resultado = ((A + B) ** 2) / 3
print(f"\nEl resultado de la expresión es: {resultado}")


# Ejercicio 8 (calcular numero de segundos en un determinado numero de dias) 
# 1 dia = 24 horas; 1 hora = 60 minutos; 1 minuto = 60 segundos
dias = int(input("¿Cuántos días quieres convertir a segundos?"))
segundos = dias * 24 * 60 * 60
print(f"\nEl número de segundos en {dias} días es: {segundos} segundos")    


# Ejercicio 9 (4 valores) suma = A + B + C + D; promedio = suma / 4
A = float(input("¿Cuál es el valor de A?")) 
B = float(input("¿Cuál es el valor de B?"))
C = float(input("¿Cuál es el valor de C?"))
D = float(input("¿Cuál es el valor de D?"))
suma = A + B + C + D
promedio = suma / 4
print(f"\nLa suma de los valores es: {suma}")
print(f"El promedio de los valores es: {promedio}")


# Ejercicio 10 (salario neto con total de horas trabajadas y precio por hora) descontar 8% de lo que gana
# salario neto = salario bruto - (salario bruto * 0.08)
horas_trabajadas = float(input("¿Cuántas horas trabajaste?"))
precio_por_hora = float(input("¿Cuál es el precio por hora?"))
salario_bruto = horas_trabajadas * precio_por_hora
salario_neto = salario_bruto - (salario_bruto * 0.08)
print(f"\nEl salario bruto es: {salario_bruto} $")
print(f"El salario neto es: {salario_neto} $")


#Ejercicio 11 (numero par o impar)

numero = int(input("Introduce un número entero: "))
if numero % 2 == 0:
    print(f"\nEl número {numero} es par.")
else:
    print(f"\nEl número {numero} es impar.")



# Ejercicio 12 (numero positivo o negativo)

numero = float(input("Introduce un número: "))
if numero > 0:
    print(f"\nEl número {numero} es positivo.")
else:
    print(f"\nEl número {numero} es negativo.")


# Ejercicio 13 (estado del agua en función de la temperatura)

temperatura = float(input("Introduce la temperatura del agua: "))
if temperatura < 0:
    print("El agua está en estado sólido (hielo).")
elif temperatura < 100:
    print("El agua está en estado líquido.")
else:
    print("El agua está en estado gaseoso (vapor).")



# Ejercicio 14 (año bisiesto divisibilidad por 4 y no 100 o divisibilidad por 400)

año = int(input("Introduce un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"\nEl año {año} es bisiesto.")
else:
    print(f"\nEl año {año} no es bisiesto.")


# Ejercicio 15 (Calcular la nómina semanal (salario neto) de un trabajador de una empresa).

def calcular_nomina_semanal(horas_trabajadas, precio_por_hora):
    
    Horsd_regulares = 35
    porcentaje_horas_extras = 0.25
    impuestos_20 = 0.20
    impuestos_30 = 0.30

    salario_bruto = horas_trabajadas * precio_por_hora
    horas_extras = max(0, horas_trabajadas - Horsd_regulares)   
    salario_horas_extras = horas_extras * precio_por_hora * (1 + porcentaje_horas_extras)
    salario_total = salario_bruto + salario_horas_extras
    impuestos = 0

    if salario_total < 1000:
        impuestos = 0
    elif 1000 <= salario_total <= 2000:
        impuestos = salario_total * impuestos_20
    else:
        impuestos = salario_total * impuestos_30

    salario_neto = salario_total - impuestos
    return salario_neto, impuestos

    horas_trabajadas = float(input("¿Cuántas horas trabajaste?"))
    precio_por_hora = float(input("¿Cuál es el precio por hora?"))
    salario_neto, impuestos = calcular_nomina_semanal(horas_trabajadas, precio_por_hora)
    print(f"\nEl salario neto es: {salario_neto} $")
    print(f"Los impuestos a deducir son: {impuestos} $")
    print(f"El salario bruto es: {salario_bruto} $")
    print(f"El salario total es: {salario_total} $")

    print(f"Las horas extras son: {horas_extras} horas")
    print(f"El salario por horas extras es: {salario_horas_extras} $")
    





































































































































































































































































































































































































































































































































































































































































