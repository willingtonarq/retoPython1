#ejercicio 1

""" numero = int(input("Introduce un número: "))  


print("Serie de numeros ")
suma = 0
for i in range(1,numero+1):
    suma += i
    
print("La suma de los primeros", numero, "números es:", suma)
   """ 
# ejercicio 2

""" numero = int(input("Introduce un número: "))  


print("Serie de numeros ")
suma = 0
for i in range(1,numero+1):
    suma += i**2
    
print("La suma de los primeros", numero, "números es:", suma)
     """

# Suma de los números enteros de n a m (m > n)

""" n = int(input("Introduce el valor de n: "))
m = int(input("Introduce el valor de m (debe ser mayor que n): "))

if m > n:
    suma = 0
    for i in range(n, m + 1):  # Itera desde n hasta m (incluyendo m)
        suma += i
    print(f"La suma de los números enteros de {n} a {m} es: {suma}")
else:
    print("El valor de m debe ser mayor que n.") """



    # Producto de dos números enteros utilizando sólo sumas

""" n = int(input("Introduce el valor de n: "))
m = int(input("Introduce el valor de m: "))

producto = 0
for _ in range(abs(m)):  
    producto += n  


if m < 0:
    producto = -producto

print(f"El producto de {n} y {m} es: {producto}") """



""" print("Introduce cinco valores de temperaturas:")
temperaturas = []  

for i in range(5):
    temp = float(input(f"Temperatura {i + 1}: "))
    temperaturas.append(temp)

promedio = sum(temperaturas) / len(temperaturas)  

print(f"El promedio de las temperaturas es: {promedio:.2f}")
 """

# Datos de entrada: Horas extras trabajadas por día (lunes a viernes)
# Datos de entrada: Horas extras trabajadas por día (lunes a viernes)
""" horas_extras = {
    "lunes": 2,
    "martes": 1,
    "miércoles": 3,
    "jueves": 0,
    "viernes": 2
}


valor_hora_ordinaria = 6774

valor_hora_extra = valor_hora_ordinaria * 1.75  

# Sumar todas las horas extras de la semana
total_horas_extras = sum(horas_extras.values())

# Calcular el total a pagar por horas extras
total_pagar = total_horas_extras * valor_hora_extra

# Resultados
print(f"Horas extras trabajadas: {horas_extras}")
print(f"Total de horas extras en la semana: {total_horas_extras} horas")
print(f"Valor por hora extra (incluye 75% de recargo): ${valor_hora_extra:,.0f} COP")
print(f"Total a pagar por horas extras: ${total_pagar:,.0f} COP") """


""" n = (400 - 20) // 2 + 1  # Cantidad de términos
suma_pares = n * (20 + 400) // 2
print(f"Suma (fórmula matemática): {suma_pares:,}") """



""" 
import random

# Número preestablecido (puede ser fijo o aleatorio)
numero_secreto = random.randint(1, 10)  # Aleatorio entre 1 y 10
# Alternativa: numero_secreto = 5  # Número fijo (ej. 5)

intentos = 3
adivinado = False

print("Adivina el número secreto (entre 1 y 10). Tienes 3 intentos.")

for intento in range(1, intentos + 1):
    print(f"\nIntento #{intento}")
    try:
        guess = int(input("Ingresa tu número: "))
    except ValueError:
        print("¡Error! Debes ingresar un número entero.")
        continue

    if guess == numero_secreto:
        print(f"¡Correcto! El número era {numero_secreto}.")
        adivinado = True
        break
    elif guess < numero_secreto:
        print("El número secreto es **mayor**.")
    else:
        print("El número secreto es **menor**.")

if not adivinado:
    print(f"\n¡Agotaste tus intentos! El número era {numero_secreto}.") """


""" suma = 0
contador = 0

print("Ingresa números positivos para sumar y promediar.")
print("El programa terminará si ingresas 0 o un número negativo.")

while True:
    try:
        numero = float(input("Ingresa un número: "))
    except ValueError:
        print("¡Error! Debes ingresar un número válido.")
        continue

    if numero <= 0:
        break  # Termina si es 0 o negativo
    
    suma += numero
    contador += 1

# Resultados
if contador > 0:
    promedio = suma / contador
    print(f"\nSuma total: {suma}")
    print(f"Promedio: {promedio:.2f}")  # 2 decimales
else:
    print("\nNo se ingresaron números positivos.") """

# Solicitar número al usuario
""" while True:
    try:
        numero = int(input("Ingresa un número entero positivo: "))
        if numero > 0:
            break
        else:
            print("¡Error! El número debe ser positivo.")
    except ValueError:
        print("¡Error! Debes ingresar un número entero válido.")

# Generar y mostrar la tabla de multiplicar
print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}") """