#Ejercicio #10 (Diseñar un programa que permita calcular e imprimir el salario neto de un trabajador conociendo el número de horas trabajadas y el precio de la hora, y teniendo en cuenta que se le va a descontar el 8% de lo que se gana).

# Leer el número de horas trabajadas y el precio de la hora
horas_trabajadas = float(input("Por favor, ingrese el número de horas trabajadas: "))
precio_hora = float(input("Por favor, ingrese el precio de la hora: $"))

# Calcular el salario bruto
salario_bruto = horas_trabajadas * precio_hora

# Calcular el descuento
descuento = salario_bruto * 0.08

# Calcular el salario neto
salario_neto = salario_bruto - descuento

print(f"\nEl salario bruto es: ${salario_bruto:.3f}")
print(f"El descuento aplicado es: ${descuento:.3f}")
print(f"El salario neto es: ${salario_neto:.3f}")

