#par o impar

"""numero =int(input("Ingresa un numero: "))
if numero %2 == 0: 
    print("Es par")
else:
    print("Es impar")"""

"""numero= int(input("Digite un numero: "))
if numero<0:
    print("Es negativo")
else:
    print("Es positivo")"""

"""temperatura=int(input("Ingrese la temperatura: "))
if temperatura<100:
    print("Es solido")
elif temperatura>=100:
    print("Es gas")
else:
    print("Es liquido")"""

"""def año_bisiesto(año):
    if (año %4 ==0 and año %100 !=0) or (año %400 ==0):
        print("El año es bisiesto")
    else:
        print("No es bisiesto")   
año_bisiesto(2005)"""

HorasTrabajadas = int(input("Ingrese las horas trabajadas: "))
PrecioHora = int(input("Ingrese el precio por hora: "))

HorasTrabajadas = int(input("ingrese las horas trabajadas: "))
PrecioHora = int(input("ingrese el precio por hora: "))


if HorasTrabajadas > 35:
    HorasNormales = 35
    HorasExtras = HorasTrabajadas - 35
    PrecioPagarHora = HorasNormales * PrecioHora
    PagoHorasExtras = HorasExtras * PrecioHora * 1.25
else:
    HorasExtras = 0
    PrecioPagarHora = HorasTrabajadas * PrecioHora
    PagoHorasExtras = 0

PrecioFinal = PrecioPagarHora + PagoHorasExtras

Descuento20 = PrecioFinal * 0.20
Descuento30 = PrecioFinal * 0.30

if (HorasTrabajadas >= 35):
    print("Se le pagará:", PrecioFinal)

elif (PrecioFinal < 1000):
    print("Su sueldo está libre de impuestos y se le pagará:", PrecioFinal)

elif (1000 <= PrecioFinal < 2000):
    print("Su sueldo será:", PrecioFinal - Descuento20)

elif (PrecioFinal > 2000):
    print("Su sueldo será:", PrecioFinal - Descuento30)


