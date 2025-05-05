#Escribir un algoritmo que calcule la suma de los cuadrados de los n primeros números 
#naturales: 12 + 22 + 32 +... + n2.

""" 
#for
n = int(input("Ingresa un número: "))
suma = 0
for i in range(1, n + 1):
    suma += i ** 2
print("La suma de los cuadrados de los primeros", n, "números naturales es:", suma) """


#while
n = int(input("Ingresa un número: "))
i = 1
suma = 0
while i <= n:
    suma += i ** 2
    i += 1
print("La suma de los cuadrados de los primeros", n, "números naturales es:", suma)    