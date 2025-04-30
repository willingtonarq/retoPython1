#Ejercicio #06 (Un estudiante tiene 4 notas, se desea calcular la nota definitiva, teniendo en cuenta que la primera nota equivale al 30%, la segunda equivale al 30%, la tercera al 25% y la última al 15%. Diseñar un programa que permita calcular e imprimir la nota definitiva del estudiante). 

# Leer las notas
nota1 = float(input("Por favor, ingrese la primera nota: "))
nota2 = float(input("Por favor, ingrese la segunda nota: "))
nota3 = float(input("Por favor, ingrese la tercera nota: "))
nota4 = float(input("Por favor, ingrese la cuarta nota: "))

# Calcular la nota definitiva
nota_definitiva = (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.25) + (nota4 * 0.15)
print(f"\nLa nota definitiva del estudiante es: {nota_definitiva:.2f}")

