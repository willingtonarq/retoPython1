# edad = input("tu edad es ")
# edad = int(edad)
# peso = input("ingresa tu peso")
# peso = int(peso)


# print("edad es ", edad)
# print ("tu peso es ", peso)
# ---------------------------------------------------

# base = input("Cual es la base ")
# base = int (base)

# altura = input("Cual es la altura ")
# altura = int (altura)

# area = (base*altura)/2

# print("El area es ", area)
# ---------------------------------------------------
# radio = input("ingresa el radio del circulo")
# radio = int (radio)

# area = radio * radio * 3.14159265359

# print("El area de tu circulo es ", area)

# ---------------------------------------------------
# pesok = input("ingresa tu peso")
# pesok = int (pesok)
# libras = pesok * 2.20462
# print("tu peso en libras es ", libras,"libras")

# ---------------------------------------------------
# precio = input("cuanto fue el valor de tu compra ")
# precio = int(precio)
# descuento = (precio * 10)/100
# aplicado = precio-descuento
# print("el descuento es  ", descuento)
# print("tu descuento aplicado es de", aplicado )
# ---------------------------------------------------

# nota1 = float (input("ingresa tu primer nota"))
# nota1 = (nota1 * 0.30)

# nota2 = float(input("ingresa tu segunda nota"))
# nota2 = (nota2 * 0.30)

# nota3 = float (input("ingresa tu tercera nota"))
# nota3 = (nota3 * 0.25)

# nota4 = float(input("ingresa tu cuarta nota"))
# nota4 = (nota4 * 0.15)

# nota = (nota1 + nota2 + nota3 + nota4)
# print("tu nota total es de ", nota)

# ---------------------------------------------------


# a =int( input("ingresa el valor de A"))
# b = int(input ("ingresa el valor de B"))
# formula= ( (a + b)**2)/3
# print("tu resultado, utilizando la formula es ", formula) 
# # ---------------------------------------------------

# dias = int(input("ingresa tu numero de dias"))
# segundos = (dias * 86.400)
# print("tus dias ", dias , " a segundos es ", segundos)

# # ---------------------------------------------------
# dato1 = int (input("ingresa tu primer nota"))
# dato2 = int (input("ingresa tu segunda nota"))
# dato3 = int (input("ingresa tu tercera nota"))
# dato4 = int (input("ingresa tu cuarta nota"))
# producto = dato1*dato2*dato3*dato4
# suma = dato1+dato2+dato3+dato4
# promedio = suma /4
# print("tu promedio es ", promedio, " tu producto es ", producto, " tu  suma es ", suma)

# # ---------------------------------------------------
# horas = float(input("ingresa el numero de horas trabajadas "))
# valor = float(input("ingresa  el valor por hora "))
# valores = (horas * valor) 
# descuento = valores * 0.08
# sueldo = (valores - descuento)
# print("tu valor neto mensual es de ",sueldo)
# # ---------------------------------------------------
# # ---------------------------------------------------
# # ---------------------------------------------------
                                #    SEGUNDA PARTE DEL TALLER, CONDICIONALES
# # ---------------------------------------------------
# # ---------------------------------------------------
# # ---------------------------------------------------

# par = int (input("ingresa un numero par o impar"))
# if (par % 2 == 0):
#     print("el numero es par")
# else :
#     print("el numero es impar ")
# ---------------------------------------------------
# numero = int(input("ingresa un numero positivo o negativo"))
# if numero > 0 :
#     print("tu numero es positivo")
# else:
#     print("tu numero es negativo")
# ---------------------------------------------------
# nivel = int(input("ingresa la temperatura del agua"))
# if nivel < 0 :
#     print("agua en estado solido")
# elif  nivel < 100:
#     print("agua en estado liquido")
# else :
#     print("agua en estado gaseoso")
# ---------------------------------------------------
# año = int (input("ingresa un año"))
# if  año % 4 == 0 and año % 100 != 0:
#     print("este numero es bisiesto")
# else :
#     print("este año no es bisiesto")
# ---------------------------------------------------

# horas = float(input("Introduce el número de horas trabajadas en la semana: "))
# precio_hora = float(input("Introduce el precio por hora (€): "))
# if horas <= 35:
#     salario_bruto = horas * precio_hora
# else:
#     horas_extras = horas - 35
#     salario_bruto = (35 * precio_hora) + (horas_extras * precio_hora * 1.25)
# salario_mensual = salario_bruto * 4
# if salario_mensual < 1000:
#     impuestos = 0
# elif salario_mensual <= 2000:
#     impuestos = 0.20 * salario_bruto
# else:
#     impuestos = 0.30 * salario_bruto
# salario_neto = salario_bruto - impuestos
# print("\nSalario bruto semanal:", salario_bruto, "€")
# print("Impuestos semanales:", impuestos, "€")
# print("Salario neto semanal:", salario_neto, "€")
