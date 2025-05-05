#Un estudiante tiene 4 notas, se desea calcular la nota definitiva, teniendo en
#cuenta que la primera nota equivale al 30%, la segunda equivale al 30%, la tercera
#al 25% y la última al 15%. Diseñar un programa que permita calcular e imprimir la
#nota definitiva del estudiante.

# Ejercicio 6 (calcular 4 notas) primera nota =0.3, segunda =0.3; tercera =0.25; cuarta =0.15
nota1 = float(input("¿Cuál es la primera nota?"))
nota2 = float(input("¿Cuál es la segunda nota?"))           
nota3 = float(input("¿Cuál es la tercera nota?"))
nota4 = float(input("¿Cuál es la cuarta nota?"))
promedio = (nota1 * 0.3) + (nota2 * 0.3) + (nota3 * 0.25) + (nota4 * 0.15)
print(f"\nEl promedio es: {promedio}")  
