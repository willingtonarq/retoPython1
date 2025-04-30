# En un supermercado de la ciudad se está aplicando un descuento del 10% sobre
# las compras que hacen los clientes. Diseñar un programa que calcule y escriba el
# descuento en pesos que se hace sobre la compra y el valor total que deberá pagar
# el cliente
compra = float(input("Ingrese el valor de la compra (en pesos): "))
descuento = compra * 0.10
total = compra - descuento
print("El descuento es: ", descuento, "pesos")
print("El total a pagar es: ", total, "pesos")
