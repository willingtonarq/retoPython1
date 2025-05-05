#Ejercicio #21 (Dada las horas Extras trabajadas de una persona por día en una semana, de lunes a viernes, y la tarifa de pago. Calcular el valor total a pagar e imprimirlo por pantalla).

# Definimos la función para calcular el pago total
def calcular_pago_total(horas_extras, tarifa_por_hora):
    # Calculamos el pago total multiplicando las horas extras por la tarifa
    return horas_extras * tarifa_por_hora

print("Cálculo del pago total por horas extras trabajadas en una semana")

# Inicializamos la variable para el total de horas extras
horas_extras_totales = 0

# Inicializamos la variable para la tarifa por hora
tarifa_por_hora = 0

# Pedimos al usuario que ingrese la tarifa por hora
tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))

# Pedimos al usuario que ingrese las horas extras trabajadas de lunes a viernes
for dia in ["lunes", "martes", "miércoles", "jueves", "viernes"]:
    # Pedimos al usuario que ingrese las horas extras trabajadas en el día actual
    horas_extras_dia = float(input(f"Ingrese las horas extras trabajadas el {dia}: "))
    # Sumamos las horas extras del día actual al total de horas extras
    horas_extras_totales += horas_extras_dia

print(f"Total de horas extras trabajadas en la semana: {horas_extras_totales} horas")

# Calculamos el pago total llamando a la función
pago_total = calcular_pago_total(horas_extras_totales, tarifa_por_hora)

# Imprimimos el resultado
print(f"El valor total a pagar por horas extras es: {pago_total} unidades monetarias")

