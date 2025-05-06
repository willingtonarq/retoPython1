# 1. Calcular el producto de todos los elementos de una lista de n posiciones.
producto=1
n=int(input("Ingrese el tamaño de la lista: "))
lista=[]
for i in range(n):
    print("Ingrese el elemento",i+1,":")
    lista.append(int(input()))
for i in range(n):
    producto*=lista[i]
print("El producto de todos los elementos de la lista es:",producto)
# 2. Calcular la suma de todos los elementos de una lista de n posiciones.
suma=0
n=int(input("Ingrese el tamaño de la lista: "))
lista=[]
for i in range(n):
    print("Ingrese el elemento",i+1,":")
    lista.append(int(input()))
for i in range(n):
    suma+=lista[i]
print("La suma de todos los elementos de la lista es:",suma)
# 3. Buscar en una lista de elementos numéricos, los elementos mayores a un valor X
# dado por el usuario y mostrar cuantos se encontraron.
lista=[1,2,3,4,5,6,7,8,9,10]
cont=0
x=int(input("Ingrese un número: "))
for i in range(len(lista)):
    if lista[i]>x:
        cont+=1
print("Se encontraron",cont,"elementos mayores a",x)
# 4. Calcular la suma de todos los elementos de una lista en sus posiciones impares.
lista=[1,2,3,4,5,6,7,8,9,10]
suma=0
for i in range(len(lista)):
    if i%2!=0:
        suma+=lista[i]
print("La suma de los elementos en posiciones impares es:",suma)
# 5. Contar en una lista de elementos numéricos cuantos elementos son positivos, cuantos
# negativos y cuantos son cero.
lista=[1,-2,3,0,-4,5,0,-6,7,0]
positivos=0
negativos=0
ceros=0
for i in range(len(lista)):
    if lista[i]>0:
        positivos+=1
    elif lista[i]<0:
        negativos+=1
    else:
        ceros+=1
print("Cantidad de elementos positivos:",positivos)
print("Cantidad de elementos negativos:",negativos)
print("Cantidad de elementos cero:",ceros)
# 6. Calcular los cuadrados de todos los elementos de una lista.
lista=[1,2,3,4,5]
cuadrados=[]
for i in range(len(lista)):
    cuadrados.append(lista[i]**2)
print("Los cuadrados de los elementos de la lista son:",cuadrados)
# 7. Determinar si un número X dado por el usuario se encuentra repetido o no en una lista
# de elementos numéricos.
lista=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]
x=int(input("Ingrese un número: "))
cont=0
for i in range(len(lista)):
    if lista[i]==x:
        cont+=1
if cont>1:
    print("El número",x,"se encuentra repetido",cont,"veces en la lista.")
else:
    print("El número",x,"no se encuentra repetido en la lista.")
# 8. Buscar en una lista de elementos numéricos los elementos menores a un valor X dado
# por el usuario y mostrar las posiciones donde están ubicados.
lista=[1,2,3,4,5,6,7,8,9,10]
x=int(input("Ingrese un número: "))
posiciones=[]
for i in range(len(lista)):
    if lista[i]<x:
        posiciones.append(i)
print("Las posiciones de los elementos menores a",x,"son:",posiciones)