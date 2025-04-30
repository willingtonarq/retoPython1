'''Un estudiante tiene 4 notas, se desea calcular la nota definitiva, teniendo en 
cuenta que la primera nota equivale al 30%, la segunda equivale al 30%, la tercera 
al 25% y la última al 15%. Diseñar un programa que permita calcular e imprimir la 
nota definitiva del estudiante.'''

# Solicitar las 4 notas al estudiante
nota1 = float(input("Ingrese la primera nota (30%): "))
nota2 = float(input("Ingrese la segunda nota (30%): "))
nota3 = float(input("Ingrese la tercera nota (25%): "))
nota4 = float(input("Ingrese la cuarta nota (15%): "))

# Calcular la nota definitiva aplicando los porcentajes
nota_definitiva = (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.25) + (nota4 * 0.15)

# Mostrar el resultado
print(f"La nota definitiva del estudiante es: {nota_definitiva:.2f}")

