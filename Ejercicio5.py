#En un supermercado de la ciudad se está aplicando un descuento del 10% sobre
#las compras que hacen los clientes. Diseñar un programa que calcule y escriba el
#descuento en pesos que se hace sobre la compra y el valor total que deberá pagar
#el cliente.

# Ejercicio 5 (supermercado descuesto 10%)= precio = precio - (precio * 0.10)
compra  = float(input("¿Cuál es el precio del producto?"))
descuento =  compra * 0.10
precio_con_descuento = compra - descuento
print(f"\nEl precio con descuento es: {descuento} $")
print(f"Total pago: {precio_con_descuento} $")
