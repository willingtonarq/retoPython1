# 5) Calcular la nómina semanal (salario neto) de un trabajador de una empresa cuyo
# trabajo se paga por horas. Leer por teclado el número de horas y el precio de la hora.
# El cálculo se realiza del siguiente modo:
# • Las primeras 35 horas se pagan a la tarifa normal.
# • Las horas extras se pagan un 25% más que las normales.
# • Los impuestos a deducir a los trabajadores varían en función de su sueldo mensual.
# • Si el sueldo es menor de 1000€, libre de impuestos.
# • Si el sueldo está entre 1000€ y 2000€, los impuestos son el 20%.
# • Si el sueldo es mayor de 2000€, el 30%.
horas_trabajadas = float(input("Ingrese el número de horas trabajadas esta semana: "))
precio_hora = float(input("Ingrese el precio por hora (€): "))

if horas_trabajadas <= 35:
    salario_bruto = horas_trabajadas * precio_hora
else:
    horas_normales = 35
    horas_extras = horas_trabajadas - 35
    salario_bruto = (horas_normales * precio_hora) + (horas_extras * precio_hora * 1.25)


sueldo_mensual = salario_bruto * 4


if sueldo_mensual < 1000:
    impuestos = 0
elif 1000 <= sueldo_mensual <= 2000:
    impuestos = salario_bruto * 0.20
else:
    impuestos = salario_bruto * 0.30


salario_neto = salario_bruto - impuestos


print(f"\nSalario bruto semanal: €{salario_bruto:.2f}")
print(f"Impuestos semanales: €{impuestos:.2f}")
print(f"Salario neto semanal: €{salario_neto:.2f}")