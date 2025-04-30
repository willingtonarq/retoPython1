# Leer número de horas trabajadas y precio por hora
horas = float(input("Ingrese el número de horas trabajadas en la semana: "))
precio_hora = float(input("Ingrese el precio por hora (€): "))

# Calcular salario bruto
if horas <= 35:
    salario_bruto = horas * precio_hora
else:
    horas_normales = 35
    horas_extras = horas - 35
    salario_bruto = (horas_normales * precio_hora) + (horas_extras * precio_hora * 1.25)

# Calcular impuestos
if salario_bruto < 1000:
    impuestos = 0
elif salario_bruto <= 2000:
    impuestos = salario_bruto * 0.20
else:
    impuestos = salario_bruto * 0.30

# Calcular salario neto
salario_neto = salario_bruto - impuestos

# Mostrar resultados
print("\n--- Nómina Semanal ---")
print("Salario bruto: €", round(salario_bruto, 2))
print("Impuestos: €", round(impuestos, 2))
print("Salario neto: €", round(salario_neto, 2))