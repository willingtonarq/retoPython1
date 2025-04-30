# Solicitar al usuario el valor de la compra
compra = float(input("Ingrese el valor total de la compra: "))
print("El valor total de su compra es:", compra)

# Calcular el descuento del 10%
descuento = compra * 0.10

# Calcular el total a pagar
total_a_pagar = compra - descuento

# Mostrar los resultados
print("El descuento aplicado es: $", round(descuento, 2))
print("El total a pagar es: $", round(total_a_pagar, 2))