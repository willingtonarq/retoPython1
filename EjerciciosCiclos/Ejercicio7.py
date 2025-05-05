#Calcular y visualizar la suma y el producto de los números pares comprendidos entre 20 y 400 ambos inclusive.


# Con while
n = 20
m = 400
suma = 0
producto = 1
i = n
while i <= m:
    if i % 2 == 0:
        suma += i
        producto *= i
    i += 1
print(f"La suma de los números pares entre {n} y {m} es: {suma}")   
print(f"El producto de los números pares entre {n} y {m} es: {producto}")


# Con for
suma = 0
producto = 1    

for i in range(n, m + 1):
    if i % 2 == 0:
        suma += i
        producto *= i
print(f"La suma de los números pares entre {n} y {m} es: {suma}")
print(f"El producto de los números pares entre {n} y {m} es: {producto}")


