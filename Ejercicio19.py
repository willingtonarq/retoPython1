#Ejercicio #19 (Implementar un algoritmo que calcule el producto de dos números enteros (n*m) haciendo sólo sumas).

# Definimos la función para calcular el producto de dos números enteros usando solo sumas
def producto_con_sumas(n, m):
    resultado = 0
    for _ in range(abs(m)):
        resultado += abs(n)
    return resultado if (n >= 0 and m >= 0) or (n < 0 and m < 0) else -resultado

print("Este programa calcula el producto de dos números enteros usando solo sumas.")
n = int(input("Introduce el primer número entero: "))
m = int(input("Introduce el segundo número entero: "))
print(f"El producto de {n} y {m} es: {producto_con_sumas(n, m)}")

