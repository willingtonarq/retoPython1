# Taller 2####################################################################################

numero= int(input("ingrese un numero: "))

if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")

################################################################################################3
numero= int(input("ingrese un numero: "))
if numero < 0:
    print("el numero es negativo")
else:
    print("el numero es positivo")

###############################################################################################3

agua= int(input("ingrese la temperatura del agua: "))
if agua < 0:
    print("el agua esta solida")
elif agua >= 0 and agua < 100:  
    print("el agua esta liquida")
else:
    print("el agua esta gaseosa")

año= int(input("ingrese un año: "))
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")

##################################################################################################3

precioH= int(input("ingrese el precio por hora: "))
horas= int(input("ingrese las horas trabajadas: "))

if horas <= 35:
    sueldo= precioH * horas
    print("el sueldo es: ", sueldo)

elif horas > 35 and horas <= 40:
    sueldo= precioH * horas * 0.25
    sueldoTotal= sueldo + precioH * horas
    print("el sueldo es: ", sueldoTotal) 


    