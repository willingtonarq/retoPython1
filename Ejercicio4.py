#Hacer un programa que permita ingresar el peso de una persona en kilogramos y devolver dicho peso en libras.

# Ejercicio 4 (peso en kg a lb)= 1 kg = 2.20462 lb
peso_kg = float(input("¿Cuál es tu peso en kg?"))
peso_lb = peso_kg * 2.20462 
print(f"\nTu peso en libras es: {peso_lb} lb")
