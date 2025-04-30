#Ejercicio #05 (En un supermercado de la ciudad se está aplicando un descuento del 10% sobre las compras que hacen los clientes. Diseñar un programa que calcule y escriba el descuento en pesos que se hace sobre la compra y el valor total que deberá pagar el cliente).

# Leer el valor de la compra
valor_compra = float(input("Por favor, ingrese el valor de su compra: $"))

# Calcular el descuento
descuento = valor_compra * 0.10
total_a_pagar = valor_compra - descuento
print(f"\nEl descuento aplicado es: ${descuento:.3f}")
print(f"El total a pagar es: ${total_a_pagar:.3f}")

