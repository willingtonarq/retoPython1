#Dada las horas Extras trabajadas de una persona por día en una semana, de lunes a
#viernes, y la tarifa de pago. Calcular el valor total a pagar e imprimirlo por pantalla.


# Con for
horas_extras = []
tarifa = float(input("Ingrese la tarifa de pago por hora extra: "))         

for i in range(5):
    horas = float(input(f"Ingrese las horas extras trabajadas el día {i + 1}: "))
    horas_extras.append(horas)

total_a_pagar = sum(horas_extras) * tarifa
print(f"El total a pagar por las horas extras trabajadas es: {total_a_pagar}")                      



# Con while
horas_extras = []   
tarifa = float(input("Ingrese la tarifa de pago por hora extra: "))

contador = 0
while contador < 5:
    horas = float(input(f"Ingrese las horas extras trabajadas el día {contador + 1}: "))
    horas_extras.append(horas)
    contador += 1

total_a_pagar = sum(horas_extras) * tarifa  
print(f"El total a pagar por las horas extras trabajadas es: {total_a_pagar}")