# Determinar si es par o impar
num = int(input("Ingrese un numero: "))
parImpar = num % 2
if parImpar == 0:
    print("El numero es par")       
else:
    print("El numero es impar")

# Determinar si num es positivo o negativo
num = int(input("Ingrese un numero: "))
if num > 0:
    print("El numero es positivo")  
elif num < 0:
    print("El numero es negativo")

# Determinar estado del agua
temperatura = float(input("Ingrese la temperatura del agua: "))
if temperatura < 0:
    print("El agua esta solida")
elif temperatura > 0 and temperatura < 100:
    print("El agua esta liquida")
elif temperatura >= 100:
    print("El agua esta gaseosa")

# Si el año es bisiesto
año = int(input("Ingrese el año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

# Nomina semanal
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
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
print(f"Salario neto semanal: {salario_neto:.2f}€")

