#Taller 1################################################################################3

edad = input("Introduce tu edad: ")
edad = int(edad)
print("Tu edad es: " , edad)

peso = input("Introduce tu Peso: ")
peso = int(peso)
print("Tu peso es: " , peso)


###################################

base = input("digite la base: ")
base = int(base)

altura = input("digite la altura: ")
altura = int(altura)

area =(base*altura)/2

print("El area de su triangulo es: ", area)


###########################################

radio = input("digite el radio: ")
radio = int(radio)



area =(radio*radio)*3.1416

print("El area de su Circulo es: ", area) 

#############################################

peso = input("Introduce tu peso: ")
peso = int(peso)

pesoL= (peso* 2.2046)
print("Tu peso en libras es: " , pesoL)

####################################################

TotalC = int (input("Introduce el valor total de tu compra: "))

Descuento =(TotalC*0.1)
Total = (TotalC-Descuento)

print("Su descuento en total es: ", Total)

#####################################################

Nota1 = int(input("introduce tu 1 nota: ")) 
Nota2 = int(input("introduce tu 2 nota: ")) 
Nota3 = int(input("introduce tu 3 nota: ")) 
Nota4 = int(input("introduce tu 4 nota: ")) 

Porcentaje1 = 0.3
Porcentaje2 = 0.25
Porcentaje3 = 0.15


TotalNotas = ((Nota1*Porcentaje1)+(Nota2*Porcentaje1)+(Nota3*Porcentaje2)+(Nota4*Porcentaje3))
print("su nota final es: " , TotalNotas)

##################################################################################################

A = int(input("introduce el primer valor: "))
B = int(input("introduce el segundo valor: "))

Resultado = ((A+B)**2)/3

print("El resultado de la operacion dada es: ",Resultado)

################################################################################

NumDias = int(input("Intruduce el numero de dias: "))

Resultados = (NumDias*86400)

print ("el numero de segundos que hay en esos dias es: ", Resultados)

################################################################################

Valor1 = int(input("introduce ti valor 1: "))
Valor2 = int(input("introduce ti valor 2: "))
Valor3 = int(input("introduce ti valor 3: "))
Valor4 = int(input("introduce ti valor 4: "))

Multi= (Valor1*Valor2*Valor3*Valor4)
print ("el resultado de la multiplicacion de todos los valores es: ", Multi)
Suma=(Valor1+Valor2+Valor3+Valor4)
print ("el resultado de la Suma de todos los valores es: ", Suma)
Prome=(Suma/4)
print ("el resultado del promedio de todos los valores es: ", Prome)

#######################################################################################

SalHora = int(input("Dame tu precio de hora trabajada: "))
HoraT= int(input("Dame las horas trabajadas: "))

TotalS = (SalHora*HoraT)
RoboBoss = (TotalS*0.08)
SalarioN=(TotalS-RoboBoss)

print("tu salario en total es: ",SalarioN)

###############################################################################################