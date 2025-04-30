""" 
# 1) Determinar si un número entero dado por el usuario es par o impar

numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")


# 2) Determinar si un número dado por el usuario es positivo o negativo

numero = float(input("Ingrese un número: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")


# 3) Determinar en qué estado está el agua en función de su temperatura.

temperatura = float(input("Ingrese la temperatura del agua en grados Celsius: "))
if temperatura < 0:
    print("El agua está en estado sólido.")
elif temperatura < 100:
    print("El agua está en estado líquido.")
else:
    print("El agua está en estado gaseoso.")


# 4) Determinar si un año es bisiesto o no.

anio = int(input("Ingrese un año: "))
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")


# 5) Calcular la nómina semanal (salario neto) de un trabajador.

horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
precio_hora = float(input("Ingrese el precio por hora: "))


if horas_trabajadas <= 35:
    salario_bruto = horas_trabajadas * precio_hora
else:
    salario_bruto = (35 * precio_hora) + ((horas_trabajadas - 35) * precio_hora * 1.25)


sueldo_mensual = salario_bruto * 4  
if sueldo_mensual < 1000:
    impuestos = 0
elif sueldo_mensual <= 2000:
    impuestos = salario_bruto * 0.20
else:
    impuestos = salario_bruto * 0.30


salario_neto = salario_bruto - impuestos

print(f"El salario neto semanal del trabajador es: {salario_neto}") """