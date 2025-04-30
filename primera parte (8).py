# Solicitar al usuario la cantidad de días
dias = int(input("Ingrese el número de días: "))

# Calcular el número de segundos
# 1 día = 24 horas, 1 hora = 60 minutos, 1 minuto = 60 segundos
segundos = dias * 24 * 60 * 60

# Mostrar el resultado
print("En", dias, "días hay", segundos, "segundos.")