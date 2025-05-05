#Dada las horas Extras trabajadas de una persona por día en una semana, de lunes a 
#viernes, y la tarifa de pago. Calcular el valor total a pagar e imprimirlo por pantalla.



# #for
""" 
horas_extras = 0  # Inicializar la variable para almacenar el total de horas extras
tarifa = float(input("Ingrese la tarifa de pago por hora extra: "))

for dia in range(1, 6):  # Iterar de lunes a viernes (5 días)
    horas = float(input(f"Ingrese las horas extras trabajadas el día {dia}: "))
    horas_extras += horas  # Sumar las horas extras del día al total


total_pago = horas_extras * tarifa  # Calcular el total a pagar
print(f"El total a pagar por horas extras es: {total_pago:.2f}")  # Imprimir el resultado """


# #while

horas_extras = 0  # Inicializar la variable para almacenar el total de horas extras
tarifa = float(input("Ingrese la tarifa de pago por hora extra: "))


dia = 1  # Inicializar el contador de días

while dia <= 5:  # Iterar de lunes a viernes (5 días)
    horas = float(input(f"Ingrese las horas extras trabajadas el día {dia}: "))
    horas_extras += horas  # Sumar las horas extras del día al total
    dia += 1  # Incrementar el contador de días


total_pago = horas_extras * tarifa  # Calcular el total a pagar
print(f"El total a pagar por horas extras es: {total_pago:.2f}")  # Imprimir el resultado
