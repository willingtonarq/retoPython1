#Ejercicio #30 (Contar en una lista de elementos numéricos cuantos elementos son positivos, cuantos negativos y cuantos son cero).

lista = []
positivos = 0
negativos = 0
cero = 0

n = int(input("Ingrese el número de elementos de la lista: "))
for i in range(n):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))
    lista.append(elemento)
    
    print(f"Elemento {i + 1}: {elemento}")
    print(f"Lista: {lista}")

    if elemento > 0:
        positivos += 1
    elif elemento < 0:
        negativos += 1
    else:
        cero += 1
    
    print("")
    print(f"Positivos: {positivos}")
    print(f"Negativos: {negativos}")
    print(f"Ceros: {cero}")
    print("")

print(f"Lista de elementos: {lista}")
print(f"Cantidad total de elementos: {len(lista)}")

