 #Calcular la suma de todos los elementos de una lista en sus posiciones impares.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista) #inicializa la lista

suma_impares = 0
print(len(lista)) #imprime la longitud de la lista

for i in range(1,11,1):
    if i % 2 != 0:
        suma_impares += lista[i]
print("La suma de los elementos en posiciones impares es:", suma_impares)



