#Para los siguientes ejercicios, después de hallar la solución al problema, desarrolle su
#correspondiente programa, utilizando estructuras de selección.
#1) Determinar si un número entero dado por el usuario es par o impar
""" numero = input("Ingrese un numero para determinar si es par o impar: ")
numero = int(numero)
if numero == 0:
    print("El numero", numero, "es cero")
elif numero%2 == 0:
    print("El numero", numero, "es par")
else:
    print("El numero", numero, "es impar")
 """

#2) Determinar si un número dado por el usuario es positivo o negativo.
""" numero = input("Ingrese un numero para determinar si es negativo o positivo: ")
numero = int(numero)
if numero == 0:
    print("El numero", numero, "es cero")
elif numero > 0:
    print("El numero", numero, "es positivo")
else:
    print("El numero", numero, "es negativo") """

#3) Determinar en qué estado está el agua en función de su temperatura. Si es negativa el
#estado será sólido, si es menor que 100 será líquido y si es 100 o mayor que 100 será
#gas. Pedir al usuario el valor de la temperatura.
""" valorTemperatura = input("Ingrese la temperatura del agua: ")
valorTemperatura = int(valorTemperatura)
if valorTemperatura < 0:
    print("El estado del agua a", valorTemperatura, "° es: Solido")
elif valorTemperatura < 100:
    print("El estado del agua a", valorTemperatura, "° es: Liquido")
else:
    print("El estado del agua a", valorTemperatura, "° es: Gas") """

#4) Un año es bisiesto si es divisible por 4 y no es divisible por 100, o es bisiesto si es
#divisible por 400. Escribir un algoritmo que lea un año y devuelva si es bisiesto o no.
""" age = input("Ingrese el año a determinar si es bisiesto o no: ")
age = int(age)
if (age%4 == 0 and age%100 != 0) or age%400 == 0:
    print("El año", age, "es bisiesto")
else:
    print("El año", age, "no es bisiesto") """

#5) Calcular la nómina semanal (salario neto) de un trabajador de una empresa cuyo
#trabajo se paga por horas. Leer por teclado el número de horas y el precio de la hora.
#El cálculo se realiza del siguiente modo:
#• Las primeras 35 horas se pagan a la tarifa normal.
#• Las horas extras se pagan un 25% más que las normales.
#• Los impuestos a deducir a los trabajadores varían en función de su sueldo mensual.
#• Si el sueldo es menor de 1000€, libre de impuestos.
#• Si el sueldo está entre 1000€ y 2000€, los impuestos son el 20%.
#• Si el sueldo es mayor de 2000€, el 30%
horasTrabajadas = input("Ingrese las horas trabajadas: ")
horasTrabajadas = float(horasTrabajadas)
valorHora = input("Ingrese el valor de la hora: ")
valorHora = float(valorHora)
salario = float()
salarioNeto = float()

if horasTrabajadas < 35:
    print(f"Horas trabajadas: {horasTrabajadas:.0f} horas < 35 horas \nTarifa: normal")
    salario = horasTrabajadas*valorHora
    print(f"Horas normales: {horasTrabajadas:.0f} horas \nValor hora: {valorHora:.2f}€")
else:
    print(f"Horas trabajadas: {horasTrabajadas:.0f} horas > 35 horas \nTarifa: 25% horas extras")
    horasExtras = +(horasTrabajadas-35)
    horasExtras = float(horasExtras)
    valorHoraExtra = valorHora + (valorHora*0.25)
    salarioNormal = valorHora*35
    salarioExtra = valorHoraExtra*horasExtras
    salario = salarioNormal + salarioExtra
    print(f"Horas normales: 35 horas \nValor hora normal: {valorHora:.2f}€ \nValor horas normales: {salarioNormal:.2f}€ \nHoras extras: {horasExtras:.0f} horas \nValor hora extra: {valorHoraExtra:.2f}€ \nValor horas extras: {salarioExtra:.2f}€")

print(f"Salario: {salario:.2f}€")

if salario < 1000:
    salarioNeto = salario
    print(f"Libre de impuestos \nSalario neto: {salarioNeto:.2f}€")
elif salario < 2000:
    impuesto = salario*0.2
    salarioNeto = salario-impuesto
    print(f"Impuesto a deducir (20%): {impuesto:.2f}€")
else:
    impuesto = salario*0.3
    salarioNeto = salario-impuesto
    print(f"Impuesto a deducir (30%): {impuesto:.2f}€")

print(f"Salario neto: {salarioNeto:.2f}€")