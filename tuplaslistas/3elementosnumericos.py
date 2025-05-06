#Buscar  en  una  lista  de  elementos  numéricos,  los  elementos  mayores  a  un  valor  X 
#dado por el usuario y mostrar cuantos se encontraron. 
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista) #inicializa la lista

contador = 0
x = int(input("Ingrese un valor: ")) 
#pide el valor al usuario

for i in lista: #recorre la lista
    if i > x: #si el elemento es mayor al valor dado por el usuario
        contador += 1 #incrementa el contador
        
print("Se encontraron", contador, "elementos mayores a", x) #muestra el resultado


