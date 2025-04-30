# Pedir al usuario el valor de la temperatura
temperatura = float(input("Ingrese la temperatura del agua en grados Celsius: "))

# Determinar el estado del agua
if temperatura < 0:
    print("El agua está en estado sólido (hielo).")
elif temperatura < 100:
    print("El agua está en estado líquido.")
else:
    print("El agua está en estado gaseoso (vapor).")