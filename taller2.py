#Ejercicio 1
def parImpar(a):
    if (a % 2 == 0):
        print("Es par")
    else:
        print("Es impar")

#Ejercicio 2
def PosOrNeg(a):
    if (a < 0):
      print("El numero es negativo")
    else:
       print("El numero es positivo")

#Ejercicio 3
def estadoAgua(a):
    if (a < 0):
        print("Está en estado solido")
    elif (0 < a < 100):
        print("Está en estado liquido")
    elif (a >= 100):
        print("Está en estado gaseoso")
    else:
        print("que coño es eso")

#Ejercicio 4
def bisiesto(a):
    if (a % 4 == 0 and a % 100 != 0 or (a % 400 == 0)):
        print("es bisiesto")
    else:
        print("no es bisiesto")

#Ejercicio 5
def salario(horas, precioHora):
    restHoras = horas - 35

    salarioNormal = 35 * precioHora

    porcentajeExtra = precioHora * 0.25

    precioHoraExtra = precioHora + porcentajeExtra

    if restHoras > 0:
        salarioExtra = restHoras * precioHoraExtra
    else:
        salarioExtra = 0  # Añadimos esta línea

    salarioFinal = salarioNormal + salarioExtra

    print(f"Su salario es {salarioFinal}")

    if (salarioFinal < 1000):
        print("Libre de impuestos")
    elif (1000 <= salarioFinal < 2000):
        impuestos = salarioFinal * 0.2
        salarioFinal = salarioFinal - impuestos
        print(f"Su sueldo tuvo el 20% de impuestos, quedo en: {salarioFinal}")
    elif (salarioFinal >= 2000):
        impuestos = salarioFinal * 0.3
        salarioFinal = salarioFinal - impuestos
        print(f"Su sueldo tuvo el 30% de impuestos, quedo en: {salarioFinal}")

salario(30, 10)