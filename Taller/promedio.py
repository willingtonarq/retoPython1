#Diseñar un algoritmo que calcule y muestre el promedio de cinco valores de 
#temperaturas dadas por el usuario



# #for
""" n = 5
suma = 0
for i in range(n):
    temperatura = float(input("Ingresa la temperatura: "))
    suma += temperatura
promedio = suma / n
print("El promedio de las temperaturas es:", promedio) """

# #while
n = 5
suma = 0
i = 0
while i < n:
    temperatura = float(input("Ingresa la temperatura: "))
    suma += temperatura
    i += 1
promedio = suma / n
print("El promedio de las temperaturas es:", promedio)

