Lista = [-4, -5, -3, -2, -1, 0, 1, 2, 3]
lista_Positivo = []
contadorPositivo = 0
lista_Negativos = []
contadorNegativo = 0
lista_Cero = []
contadorCero = 0

for i in Lista:
    if i == 0:
        lista_Cero.append(i)
        contadorCero += 1
    elif i > 0:  
        lista_Positivo.append(i)
        contadorPositivo += 1
    elif i < 0:  
        lista_Negativos.append(i)
        contadorNegativo += 1

print("Hay", contadorCero, "cero en total")
print(lista_Cero)  
print("Hay", contadorPositivo, "numeros positivos en total")
print(lista_Positivo)   
print("Hay", contadorNegativo, "numeros negativos en total")
print(lista_Negativos)   
