#Determinar en qué estado está el agua en función de su temperatura. Si es negativa el
#estado será sólido, si es menor que 100 será líquido y si es 100 o mayor que 100 será
#gas. Pedir al usuario el valor de la temperatura.


# Ejercicio 13 (estado del agua en función de la temperatura)
temperatura = float(input("Introduce la temperatura del agua: "))
if temperatura < 0:
    print("El agua está en estado sólido (hielo).")
elif temperatura < 100:
    print("El agua está en estado líquido.")
else:
    print("El agua está en estado gaseoso (vapor).")
    