""" Contar en una lista de elementos numéricos cuantos elementos son positivos, cuantos negativos y cuantos son cero. """

lista = [1, 2, 0, 3, 4, 5, 6, -2, -3, -9, 0]
contpositivos = 0
contnegativos = 0
contceros = 0

for i in range(len(lista)):
    if lista[i] > 0:
        contpositivos += 1
    elif lista[i] < 0:
        contnegativos += 1
    else:
        contceros += 1
print(f"Se encontraron {contpositivos} elementos positivos.")
print(f"Se encontraron {contnegativos} elementos negativos.")
print(f"Se encontraron {contceros} elementos que son ceros.")
