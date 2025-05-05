#Diseñar un programa que permita calcular e imprimir el salario neto de un
#trabajador conociendo el número de horas trabajadas y el precio de la hora, y
#teniendo en cuenta que se le va a descontar el 8% de lo que se gana.

# Ejercicio 10 (salario neto con total de horas trabajadas y precio por hora) descontar 8% de lo que gana
# salario neto = salario bruto - (salario bruto * 0.08)
horas_trabajadas = float(input("¿Cuántas horas trabajaste?"))
precio_por_hora = float(input("¿Cuál es el precio por hora?"))
salario_bruto = horas_trabajadas * precio_por_hora
salario_neto = salario_bruto - (salario_bruto * 0.08)
print(f"\nEl salario bruto es: {salario_bruto} $")
print(f"El salario neto es: {salario_neto} $")

