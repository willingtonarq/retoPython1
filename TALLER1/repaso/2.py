# Escribir un programa que calcule el área de un triángulo recibiendo como 
# entrada el valor de base y altura. Área= base*altura/2 

base = input("Ingresa el valor de la base: ")
base = int(base)

altura = input("Ingresa el valor de la altura: ")
altura = int(altura)

area = int((base * altura) / 2)

print(f"El valor del area del triangulo es: {area}")