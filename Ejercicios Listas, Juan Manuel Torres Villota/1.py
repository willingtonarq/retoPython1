lista_producto = []
Producto = 1

while True:
    agregar = int(input("Escribe un numero: "))
    if agregar == 0:
        break
    lista_producto.append(agregar)
    Producto *= agregar

print(lista_producto)
print(Producto)