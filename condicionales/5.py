''' Calcular la nómina semanal (salario neto) de un trabajador de una empresa cuyo 
trabajo se paga por horas. Leer por teclado el número de horas y el precio de la hora. 
El cálculo se realiza del siguiente modo: 
• Las primeras 35 horas se pagan a la tarifa normal. 
• Las horas extras se pagan un 25% más que las normales. 
• Los impuestos a deducir a los trabajadores varían en función de su sueldo mensual. 
• Si el sueldo es menor de 1000€, libre de impuestos. 
• Si el sueldo está entre 1000€ y 2000€, los impuestos son el 20%. 
• Si el sueldo es mayor de 2000€, el 30%. '''

horas = float(input("Ingrese el número de horas trabajadas en la semana: "))
tarifa = float(input("Ingrese el precio por hora: "))

# Calcular salario bruto semanal
if horas <= 35:
    salario_bruto = horas * tarifa
else:
    horas_extras = horas - 35
    salario_bruto = (35 * tarifa) + (horas_extras * tarifa * 1.25)

# Estimación de salario mensual
salario_mensual = salario_bruto * 4

# Calcular impuestos
if salario_mensual < 1000:
    impuestos = 0
elif salario_mensual <= 2000:
    impuestos = 0.20 * salario_bruto
else:
    impuestos = 0.30 * salario_bruto

# Calcular salario neto
salario_neto = salario_bruto - impuestos

print(f"Salario bruto semanal: {salario_bruto} €")
print(f"Impuestos aplicados: {impuestos} €")
print(f"Salario neto semanal: {salario_neto} €")

