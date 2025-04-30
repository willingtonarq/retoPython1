horas = float(input("Ingrese el numero de horas trabajadas: "))
precio_hora = float(input("Ingrese el precio por horas: "))
salario_bruto = horas * precio_hora
descuento = salario_bruto * 0.08
salario_neto = salario_bruto - descuento
print(f"Salario neto: {salario_neto}")