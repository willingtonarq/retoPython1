Temperatura = float(input("Ingrese la temperatura "))

if Temperatura < 0:
    print("El agua esta en estado solido")
elif Temperatura >= 0 and Temperatura < 100:
    print("El agua esta en estado liquido")
else:
    print("El agua esta en estado gaseoso")    
