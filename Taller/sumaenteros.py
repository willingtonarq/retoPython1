#Escribir  un  algoritmo  que  calcule  la  suma  de  los  números  enteros  de  n  a  m,  siendo 
#m>n,  utilizando  el  algoritmo  del  ejercicio  1.  Los  valores  de  n  y  m  son  dados  por  el usuario


# #for
""" n = int(input("Ingresa el valor de n: "))
m = int(input("Ingresa el valor de m (mayor que n): "))
if m > n:
    suma = 0
    for i in range(1, m + 1):
        suma += i
    print(f"La suma de los números enteros de {n} a {m} es: {suma}")
else:
    print("Error: el valor de m debe ser mayor que n.") """


# #while
n = int(input("Ingresa un número: "))
m = int(input("Ingresa otro número (mayor que el primero): "))

if m > n:
    suma = 0
    i = n  # ← Aquí se inicializa 'i'
    while i <= m:
        suma += i
        i += 1
    print(f"La suma de los números enteros de {n} a {m} es: {suma}")
else:
    print("Error: el segundo número debe ser mayor que el primero.")



