# Un estudiante tiene 4 notas, se desea calcular la nota definitiva, teniendo en
# cuenta que la primera nota equivale al 30%, la segunda equivale al 30%, la tercera
# al 25% y la última al 15%. Diseñar un programa que permita calcular e imprimir la
# nota definitiva del estudiante. 
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
nota4 = float(input("Ingrese la cuarta nota: "))
definitiva = (nota1 * 0.3) + (nota2 * 0.3) + (nota3 * 0.25) + (nota4 * 0.15)
print("La nota definitiva es:", definitiva)