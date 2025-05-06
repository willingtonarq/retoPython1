#Contar en una lista de elementos numéricos cuantos elementos son positivos, cuantos 
#negativos y cuantos son cero
lista = [1, -2, 3, 0, -5, 6, 0, -7, 8, 9]
print(lista) #inicializa la lista

positivos = 0
negativos = 0
ceros = 0
print(len(lista)) 

for i in range(0,10,1):
    if lista[i] > 0:
        positivos += 1
    elif lista[i] < 0:
        negativos += 1
    else:
        ceros += 1
print("La cantidad de elementos positivos es:", positivos)
print("La cantidad de elementos negativos es:", negativos)
print("La cantidad de elementos cero es:", ceros)


