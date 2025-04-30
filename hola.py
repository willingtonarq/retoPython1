#edad = input("Cual es tu edad:")
#edad = int(edad)
#peso = input("Cual es tu peso:")
#peso = int(peso)
#print("Tu edad es:", edad)
#print("Tu peso es:",peso,"Kg")

#base = input("cual es la medida de la base")
#base = int(base)
#altura = input("cual el la altura")
#altura = int(altura)
#area =(base*altura/2)
#print(area)


#radio = input("Digite el valor que tomara el radio")
#radio = float(radio)
#area =(radio*radio*3.1416)
#print(area)

#peso = input("Cual es su peso en Kg:")
#peso = int(peso)
#peso2 =(peso * 2.20462)
#print("Su peso de ",peso,"kg Convertido a libras es", peso2,)


#producto = input("Ingrese el valor de su compra:")
#producto = int(producto)
#descuento =(producto*0.10)
#productocondescuento =(producto-descuento)
#print("su descuento es de:",descuento)
#print("su producto con el 10% de descuento es:",productocondescuento )


#nota1 = float(input("Ingrese la primera nota"))
#nota2 = float(input("Ingrese la segunda nota"))
#nota3 = float(input("Ingrese la tercera nota"))
#nota4 = float(input("Ingrese la cuarta nota"))
#notaFinal = (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.25) + (nota4 * 0.15)
#print(notaFinal)


#A = input("Escriba un dato para A:")
#A = int(A)
#B = input("Escriba un dato para B:")
#B = int(B)
#C = (A+B )
#D = (C*C)
#E = (D/3)
#print(C)
#print(D)
#print(E)


#Dias = input("Digite el numero de dias")
#Dias = int(Dias)
#segundos = (Dias*86400)
#print(segundos)


#producto1 = input("Ingrese el precio de su producto1")
#producto1 = int(producto1)
#
#producto2 = input("Ingrese el precio de su producto2")
#producto2 = int(producto2)
#
#producto3 = input("Ingrese el precio de su producto3")
#producto3 = int(producto3)
#
#producto4 = input("Ingrese el precio de su producto4")
#producto4 = int(producto4)
#suma = (producto1) + (producto2) + (producto3) + (producto4)
#producto =(producto1) * (producto2) * (producto3) * (producto4)
#print("La suma de productos es:",suma)
#producto =(producto1) * (producto2) * (producto3) * (producto4)
#promedio = (suma/4)
#print("El promedio es:" ,promedio)
#print(producto)




#pagoPorHora = float(6000)
#horasTrabajadas = input("Cuantas Horas ha trabajado? :")
#horasTrabajadas = int(horasTrabajadas)
#pagoneto = (horasTrabajadas * pagoPorHora)
#print("Su pago neto es:",pagoneto)
#pagoReal =(pagoneto*0.8)
#print("Su pago real es",pagoReal)

#====SEGUNDO TALLER====#
#000000000000000000000000000000000000000000000000000000000000000000000#



#numero = int(input("Digite su numero entero:"))
#if numero % 2 == 0:
#    print("El numero es par")
#else:
#    print("El numero es impar")


#numero = int(input("Digite un numero entero:"))
#if numero > 0:
#    print("El numero es positivo")
#else:
#    print("El numero es negativo")



#AguaTemp = int(input("Ingrese la temperatura del Agua:"))
#if AguaTemp < 0 :
#    print("El agua esta en estado solido")
#elif AguaTemp < 100:
#    print("El agua esta en estado liquido")
#else:
#    print("esta gaseoso")


#año = int(input("Introduce un año: "))
#
#if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
#    print(f"El año {año} es bisiesto.")
#else:
#    print(f"El año {año} no es bisiesto.")




#horas_trabajadas = float(input("Introduce el número de horas trabajadas en la semana: "))
#tarifa_hora = float(input("Introduce el precio por hora: "))
#
#if horas_trabajadas <= 35:
#    salario_bruto = horas_trabajadas * tarifa_hora
#else:
#    horas_normales = 35
#    horas_extras = horas_trabajadas - 35
#    salario_bruto = (horas_normales * tarifa_hora) + (horas_extras * tarifa_hora * 1.25)
#
#salario_mensual = salario_bruto * 4
#
#if salario_mensual < 1000:
#    impuestos = 0
#elif salario_mensual <= 2000:
#    impuestos = salario_bruto * 0.20
#else:
#    impuestos = salario_bruto * 0.30
#salario_neto = salario_bruto - impuestos
#
#print(f"\nSalario bruto semanal: {salario_bruto:.2f} €")
#print(f"Impuestos aplicados: {impuestos:.2f} €")
#print(f"Salario neto semanal: {salario_neto:.2f} €")
