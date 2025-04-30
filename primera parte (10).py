# Solicitar los datos al usuario
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
precio_por_hora = float(input("Ingrese el precio por hora: "))

# Calcular el salario bruto
salario_bruto = horas_trabajadas * precio_por_hora

# Calcular el descuento del 8%
descuento = salario_bruto * 0.08

# Calcular el salario neto
salario_neto = salario_bruto - descuento

# Mostrar los resultados
print("Salario bruto: $", round(salario_bruto, 2))
print("Descuento (8%): $", round(descuento, 2))
print("Salario neto: $", round(salario_neto, 2))