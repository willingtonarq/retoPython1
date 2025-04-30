'''Diseñar un programa que permita calcular e imprimir el salario neto de un 
trabajador conociendo el número de horas trabajadas y el precio de la hora, y 
teniendo en cuenta que se le va a descontar el 8% de lo que se gana. '''

# Solicitar al usuario las horas trabajadas y el precio por hora
horas = float(input("Ingrese el número de horas trabajadas: "))
precio_hora = float(input("Ingrese el precio por hora: "))

# Calcular el salario bruto (sin descuento)
salario_bruto = horas * precio_hora

# Calcular el descuento del 8%
descuento = salario_bruto * 0.08

# Calcular el salario neto (con descuento)
salario_neto = salario_bruto - descuento

# Mostrar los resultados
print(f"Salario bruto: ${salario_bruto:.2f}")
print(f"Descuento (8%): ${descuento:.2f}")
print(f"Salario neto: ${salario_neto:.2f}")
