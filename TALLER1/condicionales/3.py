''' Determinar en qué estado está el agua en función de su temperatura. Si es negativa el estado será sólido, si es menor que 100 será líquido y si es 100 o mayor que 100 será gas. Pedir al usuario el valor de la temperatura.'''

temperatura = input("Ingresa la temperatura: ")
temperatura = int(temperatura)

if temperatura <= 0:
    print("El estado del agua es sólido.")
elif temperatura < 100:
    print("El estado del agua es líquido.")
else: 
    print("El estado del agua es gaseoso.")
