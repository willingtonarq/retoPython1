Año = int(input("Ingrese el año "))

if Año %4 == 0 and Año %100 != 0 or Año %400 == 0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")    