#1
#num = int(input("Ingrese un número: "))
#if num % 2 == 0:
#    print("Número par")
#else:
#    print("Número impar")

#2
#num = int(input("Ingrese un número: "))
#if num > 0:
#    print("Número positivo")
#elif num == 0:
#    print("Número 0")
#else:
#    print("Número negativo")

#3
#temp = int(input("Ingrese la temperatura del agua: "))
#if temp < 0:
#    print("Agua en estado solido")
#elif temp >= 0 and temp < 100:
#    print("Agua en estado liquido")
#else:
#    print("Agua en estado gaseoso")

#4
año = int(input("Ingresa el año: "))
if año % 4 == 0 and año % 100 != 0:
    print("Año bisiesto")
else:
    print("Año no-bisiesto")