
# Taller 1

# Ejercicio 1
edad = input("ingrese su edad: ")
peso = input("ingrese su peso: ")

print(f"Tu edad es: {edad} y tu peso es: {peso}")

# Ejercicio 2
base = input("ingrese la base del triangulo: ")
altura = input("ingrese la altura del triangulo: ")
operacion = (int(base) * int(altura)) / 2
print(f"El area del triangulo es: {operacion}")

# Ejercicio 3
radio = input("Escribe el radio del circulo")
radio = int(radio)
area = radio*radio/3.1416
print(f"El area del circulo es {area}")

# Ejercicio 4
peso = input("Ingresa tu peso: ")
operacion = int(peso) * 2.20462
print(f"Tu peso en kilogramos es: {operacion}")

# Ejercicio 5
compra = input("ingrese el valor de su compra: ")
descuento = int(compra) * 0.1
valorFinal = int(compra) - descuento
print(f"El valor final de al compra es: {valorFinal}")

# Ejercicio 6
nota1 = int(input("ingrese nota: "))
nota2 = int(input("ingrese nota: "))
nota3 = int(input("ingrese nota: "))
nota4 = int(input("ingrese nota: "))

operacion = nota1 * 0.3 + nota2 * 0.3 + nota3 * 0.25 + nota4 * 0.15
print(f"Su nota definitva es: {operacion}")

# Ejercicio 7
a = input("valor A: ")
b = input("valor B: ")
a = int(a)
b = int(b)
operacion = (a * b)*(a * b)/3
print(f"Resultado: {operacion}")

# Ejercicio 8
dias = int(input("Ingresa el numero de días: "))
operacion = dias * 86400
print(f"{dias} dias a segundos, son: {operacion} segundos")

# Ejercicio 9
valor1 = int(input("ingresa un valor: "))
valor2 = int(input("ingresa un valor: "))
valor3 = int(input("ingresa un valor: "))
valor4 = int(input("ingresa un valor: "))


producto = valor1 * valor2 * valor3 * valor4
suma = valor1 + valor2 + valor3 + valor4
promedio = (valor1 + valor2 + valor3 + valor4)/4

print(f"El producto de esos valores es: {producto}")
print(f"La suma de esos valores es: {suma}")
print(f"El promedio de esos valores es: {promedio}")

# Ejercicio 10
horas = int(input("Ingrese el valor de las horas tranajadas: "))
precioHora = int(input("Ingrese el valor de el preico de la hora: "))

salario = horas * precioHora
descuento = salario * 0.08
salarioFinal = salario - descuento

print(f"Su descuento es final es: {descuento}") 
print(f"Su salario final es: {salarioFinal}") 