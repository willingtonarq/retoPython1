""" Dada las horas Extras trabajadas de una persona por día en una semana, de lunes a 
viernes, y la tarifa de pago. Calcular el valor total a pagar e imprimirlo por pantalla.  """

# CICLO FOR

""" horas_extras = []
for dia in ["lunes", "martes", "miércoles", "jueves", "viernes"]:
    horas = float(input(f"Ingrese las horas extras trabajadas el {dia}: "))
    horas_extras.append(horas)

tarifa = 7736

# Calcular el valor total a pagar
valor_total = sum(horas_extras) * tarifa

# Imprimir el resultado
print(f"El valor total a pagar por las horas extras trabajadas es: {valor_total}")
 """
# CICLO WHILE

tarifa = 7736
valor_total = 0

dice = ["lunes", "martes", "miércoles", "jueves", "viernes"]
contador = 0

while contador < len(dice):
    dia = dice[contador]
    horas = float(input(f"Ingrese las horas extras trabajadas el {dia}: "))
    valor_total += horas * tarifa
    contador += 1

# Imprimir el resultado
print(f"El valor total a pagar por las horas extras trabajadas es: {valor_total}")