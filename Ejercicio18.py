#Ejercicio #18 (Escribir un algoritmo que calcule la suma de los números enteros de n a m, siendo m>n, utilizando el algoritmo del ejercicio 1. Los valores de n y m son dados por el usuario).

# Definimos la función para calcular la suma de los números enteros de n a m

def suma_enteros_n_a_m(n, m):
    suma = 0
    for i in range(n, m + 1):
        suma += i
    return suma

print("Este programa calcula la suma de los números enteros de n a m.")
n = int(input("Introduce el valor de n (menor que m): "))
m = int(input("Introduce el valor de m (mayor que n): "))
print(f"La suma de los números enteros de {n} a {m} es: {suma_enteros_n_a_m(n, m)}")