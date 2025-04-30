#Ejercicio #15 (Calcular la nómina semanal (salario neto) de un trabajador de una empresa cuyo trabajo se paga por horas. Leer por teclado el número de horas y el precio de la hora. El cálculo se realiza del siguiente modo:
#• Las primeras 35 horas se pagan a la tarifa normal.
#• Las horas extras se pagan un 25% más que las normales.
#• Los impuestos a deducir a los trabajadores varían en función de su sueldo mensual.
#• Si el sueldo es menor de 1000€, libre de impuestos.
#• Si el sueldo está entre 1000€ y 2000€, los impuestos son el 20%.
#• Si el sueldo es mayor de 2000€, el 30%.)

# Solicitamos datos al usuario.
horas_trabajadas = float(input("Introduce el número de horas trabajadas: "))
precio_por_hora = float(input("Introduce el precio por hora: "))

# Calcular el salario bruto.
if horas_trabajadas <= 35:
    salario_bruto = horas_trabajadas * precio_por_hora
else:
    horas_extras = horas_trabajadas - 35
    salario_bruto = (35 * precio_por_hora) + (horas_extras * precio_por_hora * 1.25)

# Calcular impuestos.
if salario_bruto < 1000:
    impuestos = 0
elif salario_bruto <= 2000:
    impuestos = salario_bruto * 0.20
else:
    impuestos = salario_bruto * 0.30

# Calcular salario neto.
salario_neto = salario_bruto - impuestos

# Mostrar resultados.
print(f"Salario bruto: {salario_bruto:.3f}€")
print(f"Impuestos: {impuestos:.3f}€")
print(f"Salario neto: {salario_neto:.3f}€")
