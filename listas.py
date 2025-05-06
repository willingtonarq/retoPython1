#Calcular el producto de todos los elementos de una lista de n posiciones.

""" lista = [1, 2, 3, 4, 5]
total = 1
for elemento in lista:
    total *= elemento
print(total) """

# Calcular la suma de todos los elementos de una lista de n posiciones.

""" lista = [1, 2, 3, 4, 5]
suma = 0 
for elemento in lista:
    suma += elemento
print(suma)
 """


#Buscar en una lista de elementos numéricos, los elementos mayores a un valor X
#dado por el usuario y mostrar cuantos se encontraron.

""" lista = [1, 2, 3, 4, 5]
numero = 2
contador = 0
elemento = 0
for elemento in lista:
    if elemento > numero:
    
        contador += 1

print("Los elementos mayores a", numero, "son:", contador) """

""" 
total = 0
lista = [1,2,3,4,5,6,7,8,9,10]
for contador in lista:
    if contador % 2 == 0:
        print("El elemento es par")
    else:
        total += contador

print (total )
 """

""" tamaño = int(input("Cuantos numeros quieres ingresar: "))
lista = [tamaño]
for i in range(tamaño):
    number = int(input("Introduce un numero: "))
    lista.append(number)
    if number > 0:
        print ("el numero es positivo")
    elif number < 0:
        print ("el numero es negativo")
    else:
            print ("el numero es cero") """


""" lista = [1, 2, 3, 4, 5]
acumulador = 0
for elemento in lista:
    acumulador += elemento **2
print(acumulador) """


lista = [1, 2, 3, 4, 5]

numero = int(input("Ingrese un número: "))
for elemento in lista:
    if numero == elemento:
        print("El número ya existe en la lista.")
        
        break
    else:
        print("el numero no esta ne la lista")


