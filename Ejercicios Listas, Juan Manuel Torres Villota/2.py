lista_Suma = []
Suma = 0

while True:
    agregar = int(input("Escribe un numero: "))
    if agregar == 0:
        break
    lista_Suma.append(agregar)
    Suma += agregar

print(lista_Suma)
print(Suma)