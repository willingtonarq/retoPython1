Horas = int(input("Ingrese las horas trabajadas "))
precioHora = 6200
Descuento = 0.08
Salario = ""

Salario = Horas * precioHora
SalarioNeto = Salario - (Salario * Descuento)
print("tu salario en base a las horas trabajadas es de", SalarioNeto)