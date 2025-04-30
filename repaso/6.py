''' Un estudiante tiene 4 notas, se desea calcular la nota definitiva, teniendo en 
cuenta que la primera nota equivale al 30%, la segunda equivale al 30%, la tercera 
al 25% y la última al 15%. Diseñar un programa que permita calcular e imprimir la 
nota definitiva del estudiante. Elaborar el algoritmo en pseudocódigo. '''

nota1 = input("Ingresa la nota 1: ")
nota1 = float(nota1)

nota2 = input("Ingresa la nota 2: ")
nota2 = float(nota2)

nota3 = input("Ingresa la nota 3: ")
nota3 = float(nota3)

nota4 = input("Ingresa la nota 4: ")
nota4 = float(nota4)

promedio1 = nota1 * 0.3
promedio2 = nota2 * 0.3
promedio3 = nota3 * 0.25
promedio4 = nota4 * 0.15

notaDefinitiva = promedio1 + promedio2 + promedio3 + promedio4
print(f"La nota definitiva del estudiante es {notaDefinitiva}")