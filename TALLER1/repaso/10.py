''' Diseñar un programa que permita calcular e imprimir el salario neto de un 
trabajador conociendo el número de horas trabajadas y el precio de la hora, y 
teniendo en cuenta que se le va a descontar el 8% de lo que se gana. '''

horasTrabajadas = input("Ingresa el número de horas trabajadas: ")
horasTrabajadas = int(horasTrabajadas)

horaLaboral = 6189
salarioCalculado = horasTrabajadas * horaLaboral

278.505
22.280

descuento = (salarioCalculado * 0.08)
salarioNeto = round(salarioCalculado - descuento)
print(f"El salario final del trabajador es ${salarioNeto}")

