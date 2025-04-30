
'''


numero = input("Ingrese un numero: ")
numero = int(numero)
if numero % 2 == 0:
    print('numero par')
else:
    print ('numero impar')



numero = input("Ingrese un numero: ")
numero = int(numero)

if numero >= 0:
    print('numero positivo')
else:
    print('numero negativo')


temperatura = input("Ingrese la temperatura: ")
temperatura = int(temperatura)
if temperatura < 0:
    print('El estado del agua es solido')
elif temperatura < 100:
    print('El estado del agua es liquido')
else:
    print('El estado del agua es gaseoso')

#Un año es bisiesto si es divisible por 4 y no es divisible por 100, o es bisiesto si es
#divisible por 400. Escribir un algoritmo que lea un año y devuelva si es bisiesto o no.

anio = input("Ingrese un año: ")
anio = int(anio)
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print('El año es bisiesto')
else:
    print('El año no es bisiesto')


Calcular la nómina semanal (salario neto) de un trabajador de una empresa cuyo
trabajo se paga por horas. Leer por teclado el número de horas y el precio de la hora.
El cálculo se realiza del siguiente modo:
• Las primeras 35 horas se pagan a la tarifa normal.
• Las horas extras se pagan un 25% más que las normales.
• Los impuestos a deducir a los trabajadores varían en función de su sueldo mensual.
• Si el sueldo es menor de 1000€, libre de impuestos.
• Si el sueldo está entre 1000€ y 2000€, los impuestos son el 20%.
• Si el sueldo es mayor de 2000€, el 30%.
'''

horas = input("Ingrese el numero de horas trabajadas: ")
horas = int(horas)
precio_hora = input("Ingrese el precio por hora: ")
precio_hora = int(precio_hora)
if horas <= 35:
    sueldo = horas * precio_hora
else:
    sueldo = (35 * precio_hora) + ((horas - 35) * precio_hora * 1.25)
if sueldo < 1000:
    sueldo_neto = sueldo
elif sueldo < 2000:
    sueldo_neto = sueldo * 0.8
else:
    sueldo_neto = sueldo * 0.7
print('El sueldo neto es: ', sueldo_neto)

