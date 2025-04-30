# 1) Determinar si un número entero dado por el usuario es par o impar
numero=int(input("Ingrese un número entero: "))
if numero%2==0:
    print("El número es par")
else:
    print("El número es impar")
# 2) Determinar si un número dado por el usuario es positivo o negativo.
numero=float(input("Ingrese un número: "))
if numero>0:
    print("El número es positivo")
elif numero<0:
    print("El número es negativo")
# 3) Determinar en qué estado está el agua en función de su temperatura. Si es negativa el
# estado será sólido, si es menor que 100 será líquido y si es 100 o mayor que 100 será
# gas. Pedir al usuario el valor de la temperatura.
temperatura=float(input("Ingrese la temperatura del agua: "))
if temperatura<0:
    print("El agua está en estado sólido")
elif temperatura<100:
    print("El agua está en estado líquido")
else:
    print("El agua está en estado gaseoso")
# 4) Un año es bisiesto si es divisible por 4 y no es divisible por 100, o es bisiesto si es
# divisible por 400. Escribir un algoritmo que lea un año y devuelva si es bisiesto o no.
año=int(input("Ingrese un año: "))
if (año%4==0 and año%100!=0) or (año%400==0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
# 5) Calcular la nómina semanal (salario neto) de un trabajador de una empresa cuyo
# trabajo se paga por horas. Leer por teclado el número de horas y el precio de la hora.
# El cálculo se realiza del siguiente modo:
# • Las primeras 35 horas se pagan a la tarifa normal.
# • Las horas extras se pagan un 25% más que las normales.
# • Los impuestos a deducir a los trabajadores varían en función de su sueldo mensual.
# • Si el sueldo es menor de 1000€, libre de impuestos.
# • Si el sueldo está entre 1000€ y 2000€, los impuestos son el 20%.
# • Si el sueldo es mayor de 2000€, el 30%.
horas=float(input("Ingrese el número de horas trabajadas: "))
precio_hora=float(input("Ingrese el precio de la hora: "))
if horas<=35:
    sueldo=horas*precio_hora
else:
    horas_extras=horas-35
    sueldo=(35*precio_hora)+(horas_extras*precio_hora*1.25)
if sueldo<1000:
    impuestos=0
elif sueldo<=2000:
    impuestos=sueldo*0.20
else:
    impuestos=sueldo*0.30
sueldo_neto=sueldo-impuestos
print("El sueldo neto es: ", sueldo_neto)