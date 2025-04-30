"""Hacer un programa que permita ingresar el peso de una persona en kilogramos y 
devolver dicho peso en libras."""

def convertir_kg_a_libras(kg):
    libras = kg * 2.20462
    return libras


peso_kg = float(input("Ingresa tu peso en kilogramos: "))


peso_libras = convertir_kg_a_libras(peso_kg)

print(f"Tu peso en libras es: {peso_libras:.2f}")
