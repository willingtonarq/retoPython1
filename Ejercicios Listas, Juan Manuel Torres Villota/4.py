Lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_Impar = []
Suma = ""

for i in Lista:
     if i %2 != 0:
        lista_Impar.append(i)
        Suma = sum(lista_Impar)

          
print(Lista)          
print(lista_Impar)
print(Suma)


