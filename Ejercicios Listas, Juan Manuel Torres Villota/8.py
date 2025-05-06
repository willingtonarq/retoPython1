Lista = [2, 8, 9, 10, 14, 18, 20, 22]
lista_Menor = []
valorX = int(input("Escriba el valor X: "))


for i in Lista:
    if i < valorX:
        lista_Menor.append(i)
        print(Lista.index(i))
        

print(lista_Menor)

