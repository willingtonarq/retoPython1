#Determinar si un número X dado por el usuario se encuentra repetido o no en una lista 
#de elementos numéricos.
# Lista de números (puede tener repetidos)
numeros = [4, 7, 2, 7, 9, 4, 1]

# Pedir al usuario un número
x = int(input("Ingresa el número que quieres verificar: "))

# Contar cuántas veces aparece ese número en la lista
cantidad = numeros.count(x)

# Mostrar resultado
if cantidad > 1:
    print(f"El número {x} está repetido {cantidad} veces.")
elif cantidad == 1:
    print(f"El número {x} está en la lista pero no está repetido.")
else:
    print(f"El número {x} no está en la lista.")



