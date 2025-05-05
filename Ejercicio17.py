#Ejercicio #17 (Escribir un algoritmo que calcule la suma de los cuadrados de los n primeros números naturales: 1**2 + 2**2 + 3**2 +… + n**2).

# # Definimos la función para calcular la suma de los cuadrados de los n primeros números naturales
suma = 0
contador = 0

numero = int(input("Introduce un número entero positivo: "))    
# Usamos un bucle while para iterar hasta n y sumar los cuadrados de los números
while contador <= numero:
    suma += contador ** 2
    contador += 1

print(f"La suma de los cuadrados de los primeros {numero} números naturales es: {suma}")






