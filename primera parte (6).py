# Solicitar las 4 notas al usuario
nota1 = float(input("Ingrese la primera nota (30%): "))
nota2 = float(input("Ingrese la segunda nota (30%): "))
nota3 = float(input("Ingrese la tercera nota (25%): "))
nota4 = float(input("Ingrese la cuarta nota (15%): "))

# Calcular la nota definitiva con los respectivos porcentajes
nota_definitiva = (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.25) + (nota4 * 0.15)

# Mostrar la nota definitiva
print("La nota definitiva del estudiante es:", round(nota_definitiva, 2))