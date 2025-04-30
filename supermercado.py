"""En un supermercado de la ciudad se está aplicando un descuento del 10% sobre 
las compras que hacen los clientes. Diseñar un programa que calcule y escriba el 
descuento en pesos que se hace sobre la compra y el valor total que deberá pagar 
el cliente. Elaborar el algoritmo en pseudocódigo. """ 

# Solicitar al usuario el valor total de la compra
compra = float(input("Ingrese el valor total de la compra: "))

# Calcular el 10% de descuento
descuento = compra * 0.10

# Calcular el total a pagar después del descuento
total_pagar = compra - descuento

# Mostrar los resultados
print(f"El descuento aplicado es: ${descuento:.2f}")
print(f"El total a pagar es: ${total_pagar:.2f}")



