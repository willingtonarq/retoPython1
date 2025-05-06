""" Determinar si un número X dado por el usuario se encuentra repetido o no en una lista de elementos numéricos.  """

numero = int(input("Ingrese el número a buscar: "))
lista = [1, 2, 3, 2, 5, 6, 2, 8, 3, 10]
contador = 0

contador = lista.count(numero)

if contador > 1:
    print(f"El número {numero} está repetido {contador} veces en la lista.")
elif contador == 1:
    print(f"El número {numero} está en la lista pero no está repetido.")
else:
    print(f"El número {numero} no está en la lista.")

