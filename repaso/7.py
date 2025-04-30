''' Construya un programa tal que dados los datos enteros A y B, escriba el resultado 
de la siguiente expresión: 
(A + B)2 / 3 '''

enteroA = input("Ingresa el valor de A: ")
enteroA = int(enteroA)

enteroB = input("Ingresa el valor de B:")
enteroB = int(enteroB)

expresion = round((((enteroA + enteroB) ** 2) / 3),2)
print(f"El resultado de la operación es {expresion}")