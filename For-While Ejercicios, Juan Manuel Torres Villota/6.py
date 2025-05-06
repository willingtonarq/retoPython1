diaTrabajado = 54000
Tarifa = 6200
Suma = 0
Total = 0

for i in range (5):
    horasExtra = float(input(f"Cuantas horas extra trabajo hoy {i+1}? :" ))
    Suma += horasExtra


Total = print(Suma * Tarifa + diaTrabajado)