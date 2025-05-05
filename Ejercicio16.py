#Ejercicio #16 (Escribir un algoritmo que calcule la suma de los n primeros números naturales. Analizar si se puede implementar con los dos tipos de ciclos. El valor de n es dado por el usuario).

suma = 0
contador = 0

numero = int(input("Introduce un número entero positivo: "))
# Usamos un bucle while para iterar hasta n y sumar los números
while contador <= numero:
    suma += contador
    contador += 1

print(f"La suma de los primeros {numero} números naturales es: {suma}")





