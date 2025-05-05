#Escribir un algoritmo que calcule la suma de los n primeros números naturales.
#Analizar si se puede implementar con los dos tipos de ciclos. El valor de n es dado por el usuario.


# Con for
numero = int(input("Ingrese un número: "))  
suma = 0 
for i in range(1, numero + 1):  
    suma += i                       
print("La suma de los primeros", numero, "números naturales es:", suma)


# Con while
n = int(input("Ingrese un número natural n: "))
suma = 0
i = 1
while i <= n:
    suma += i
    i += 1
print(f"La suma de los {n} primeros números naturales es: {suma}")
