#Calcular y visualizar la suma y el producto de los números pares comprendidos entre 
#20 y 400 ambos inclusive.



#for
""" suma = 0
producto = 1
for i in range(20, 401):
    if i % 2 == 0:
        suma += i
        producto *= i
print("La suma de los números pares entre 20 y 400 es:", suma)
print("El producto de los números pares entre 20 y 400 es:", producto) 
 """
# #while
suma = 0
producto = 1
i = 20
while i <= 400:
    if i % 2 == 0:
        suma += i
        producto *= i
    i += 1
print("La suma de los números pares entre 20 y 400 es:", suma)
print("El producto de los números pares entre 20 y 400 es:", producto)
