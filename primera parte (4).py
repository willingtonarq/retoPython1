# Solicitar al usuario que ingrese el peso en kilogramos
peso_kg = float(input("Ingresa tu peso en kilogramos: "))
print("Tu peso en kilogramos es de:", peso_kg)

# Convertir a libras
peso_libras = peso_kg * 2.20462

# Mostrar el resultado
print("Tu peso en libras es:", round(peso_libras, 2))