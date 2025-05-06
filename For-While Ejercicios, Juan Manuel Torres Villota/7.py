suma = 0
producto = 1
for i in range(20, 400, 2):
    suma += i
    producto *= i
print(f"La suma de los números pares es: {suma}")   
print(f"El producto de los números pares es: {producto}")