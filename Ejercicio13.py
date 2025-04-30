#Ejercicio #13 (Determinar en qué estado está el agua en función de su temperatura. Si es negativa el estado será sólido, si es menor que 100 será líquido y si es 100 o mayor que 100 será gas. Pedir al usuario el valor de la temperatura).

Temperatura = float(input("Ingrese la temperatura del agua en grados Celsius: "))

if Temperatura < 0:
    estado = "sólido"
elif Temperatura < 100:
    estado = "líquido"
else:
    estado = "gaseoso"

print(f"El estado del agua a {Temperatura} grados Celsius es {estado}.")
print("Fin del programa")

