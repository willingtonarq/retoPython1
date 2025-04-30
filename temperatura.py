'''Determinar en qué estado está el agua en función de su temperatura. Si es negativa el
estado será sólido, si es menor que 100 será líquido y si es 100 o mayor que 100 será
gas. Pedir al usuario el valor de la temperatura.'''


# Solicitar al usuario que ingrese la temperatura
temperatura = float(input("Ingrese la temperatura del agua en grados Celsius: "))

# Determinar el estado del agua según la temperatura
if temperatura < 0:
    print("El agua está en estado sólido (hielo).")
elif temperatura < 100:
    print("El agua está en estado líquido.")
else:
    print("El agua está en estado gaseoso (vapor).")
