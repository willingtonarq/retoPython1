#Diseñe un programa que calcule e imprima el número de segundos que hay en un determinado número de días.

# Ejercicio 8 (calcular numero de segundos en un determinado numero de dias) 
# 1 dia = 24 horas; 1 hora = 60 minutos; 1 minuto = 60 segundos
dias = int(input("¿Cuántos días quieres convertir a segundos?"))
segundos = dias * 24 * 60 * 60
print(f"\nEl número de segundos en {dias} días es: {segundos} segundos")    
