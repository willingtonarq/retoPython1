# Hacer un programa que permita ingresar el peso de una persona en kilogramos y 
# devolver dicho peso en libras. 

peso = input("Ingresa tu peso en kg: ")
peso = int(peso)

pesoCalculado = round((peso * 2.20462),2)
print(f"Tu peso en libras es {pesoCalculado}")