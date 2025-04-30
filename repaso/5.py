'''En un supermercado de la ciudad se está aplicando un descuento del 10% sobre 
las compras que hacen los clientes. Diseñar un programa que calcule y escriba el 
descuento en pesos que se hace sobre la compra y el valor total que deberá pagar 
el cliente. Elaborar el algoritmo en pseudocódigo.'''

compra = input("Ingrese el valor total de la compra: ")
compra = int(compra)

descuento = int(compra * 0.10)
print(f"El descuento es de ${descuento}")

totalCompra = compra - descuento
print(f"El cliente debera pagar en total ${totalCompra}")
