# print ("Si")

# edad = input ("introduce tu edad: ")
# peso = input ("introduce tu peso: ")
# edad = int (edad) #Convierte la entrada a un entero
# peso= int (peso)
# print ("Tu edad es :" , edad ,  " 22 Y pesas : " , peso )

# #2 ejercicio

# Base = input ("introduce la base: ")
# Altura = input ("introduce la Altura: ")
# Base = int (Base)
# Altura = int (Altura)

# Area = Base * Altura/2

# print ("El area es :" , Area )

# #3 ejercicio

# radio = input ("introduce el radio 1: ")
# radio = int(radio)
# Area= radio * radio / 3.14

# print ("El radio del circulo es:" , Area)

# #4 ejercicio
# peso= input ("introduce el peso")
# peso = int(peso)
# convertir = peso * 2,205
# print ("El peso es:" , convertir)


#5 ejercicio

# producto= input ("ingrese el precio del producto: ")
# producto = int(producto)
# descuento = producto * 0.1
# preciofinal= producto - descuento
# print ("el precio final es:", preciofinal)

#6 ejercicio

# nota1= int(input ("ingrese la nota 1: "))
# nota2= int (input ("ingrese la nota 2: "))
# nota3= int (input ("ingrese la nota 3: "))
# nota4= int (input ("ingrese la nota 4: "))

# notadefinitiva = nota1* 0.3 + nota2* 0.3 + nota3 * 0.25 + nota4 * 0.15
# print("su nota es: " , notadefinitiva)

#7 ejercicio
# EnteroA = int(input("ingrese el primer entero: "))
# EnteroB = int(input("ingrese el segundo entero: "))
# resultado = EnteroA + EnteroB **2 / 3
# print ("El resultado es: " , resultado)

#8 ejercicio

# Dias = int(input("ingrese el numero de dias: " ))
# resultado = Dias * 86400
# print("Los segundos que hay en los dias ingresados es: " , resultado)

#9 ejercicio

# Producto1 = int(input("ingrese un valor: "))
# Producto2 = int(input("ingrese un valor: "))
# Producto3 = int(input("ingrese un valor: "))
# Producto4 = int(input("ingrese un valor: "))

# resultadom = Producto1 * Producto2 * Producto3 * Producto4
# print ("su producto es " , resultadom)

# resultados = (Producto1 + Producto2 + Producto3 + Producto4)
# print ("su suma es " , resultados)

# resultadop = (Producto1 + Producto2 + Producto3 + Producto4)/ 4
# print ("su promedio es " , resultadop)



#10 ejercicio
# HorasTrabajadas = int (input("ingrese las horas trabajadas: "))
# PrecioHora =int(input("ingrese el precio por hora: "))
# ValorPago= (PrecioHora * HorasTrabajadas) * 0.08
# print("El valor a pagar es:" , ValorPago)


#Ejercicios de segundo nivel

#Ejercicio 1

# def numero (a)
#     if (a % 2 ==0):
#         print("El numero es par ")
#     else:
#         print("El numero es impar")

#Ejercicio 2

# def numero (a)
#     if (a>=0):
#         print("El numero es positivo")
#     else:
#         print("El numero es negativo")

#Ejercicio 3

# def temperatura (a)
#     if (a<=0):
#         print("El estado del agua es solida")
#     elif (a<=100):
#         print("El estado del agua es liquido")
#     elif (a>=100):
#         print("El estado es gaseoso")

#Ejercicio 4
# def año_bisiesto (año):
#     if (año % 4 ==0  and año %100 !=0) or (año % 400 ==0):
#         print("El año es bisiesto")
#     else :
#         print("El año no es bisiesto")
    
# año_bisiesto (2000)


#Ejercicio 5

HorasTrabajadas = int(input("Ingrese las horas trabajadas: "))
PrecioHora = int(input("Ingrese el precio por hora: "))

if HorasTrabajadas > 35:
    HorasNormales = 35
    HorasExtras = HorasTrabajadas - 35
    PrecioPagarHora = HorasNormales * PrecioHora
    PagoHorasExtras = HorasExtras * PrecioHora * 1.25
else:
    HorasExtras = 0
    PrecioPagarHora = HorasTrabajadas * PrecioHora
    PagoHorasExtras = 0

PrecioFinal = PrecioPagarHora + PagoHorasExtras

Descuento20 = PrecioFinal * 0.20
Descuento30 = PrecioFinal * 0.30

if (HorasTrabajadas >= 35):
    print("Se le pagará:", PrecioFinal)

elif (PrecioFinal < 1000):
    print("Su sueldo está libre de impuestos y se le pagará:", PrecioFinal)

elif (1000 <= PrecioFinal < 2000):
    print("Su sueldo será:", PrecioFinal - Descuento20)

elif (PrecioFinal > 2000):
    print("Su sueldo será:", PrecioFinal - Descuento30)













