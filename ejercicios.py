# peso edad
edad=input("Ingresa tu edad: ")
edad=int(edad)
peso=input("cuanto pesas: ")
peso=float(peso)
print("tu edad ingresada es: ", edad, "tu peso ingresado es: ", peso)


# Area de un triangulo
base=input("ingresa el valor de la base: ")
base=int(base)
altura=input("ingresa el valor de la altura: ")
altura=int(altura)
area=base*altura/2
print("el resultado del area de el triangulo es: ",area)


# circulo
r1=input("ingrese el diamero del primer radio: ")
r1=float(r1)
r2=input("ingrese el diamero del segundo radio: ")
r2=float(r2)
area=r1*r2*3.141516
area=round(area, 2)
print("el area es: ", area)


# peso kg a lb
peso=input("Ingrese su peso en kilo gramos: ")
peso=float(peso)
conversion=peso*2
print("su peso en libras es: ",conversion, "Lb")


supermercado
precio=input("Ingresa el valor del producto: ")
precio=float(precio)
porcentaje = 10

resultado=(20 / 100) * precio
print(f"El {porcentaje}% de {precio} es: {resultado}")


n1=input("Ingresa la nota1")
n1=float(n1)
n2=input("Ingresa la nota2")
n2=float(n2)
n3=input("Ingresa la nota3")
n3=float(n3)
n4=input("Ingresa la nota4")
n4=float(n4)
promedio=((n1*0.3)+(n2*0.3)+(n3*25)+(n4*15))
print("la nota final es de: ", promedio)




n1=input("Ingresa el primer dijito: ")
n1=int(n1)
n2=input("Ingresa el segundo dijito: ")
n2=int(n2)
operacion=(n1 + n2)**2/3
operacion=round(operacion, 2)
print("el resultado es: ", operacion)


dias=int(input("ingresa los dias: "))
horas=dias*24
segundos=horas*3600
print(f"conversion de dias es {dias} y en horas {horas} y en segundos {segundos}")




n1=int(input("ingresa el dijito: "))
n2=int(input("ingresa el dijito: "))
n3=int(input("ingresa el dijito: "))
n4=int(input("ingresa el dijito: "))
suma=n1+n2+n3+n4
promedio=suma/4
print(f"la suma es {suma} el promedio {promedio}")



horas_trabajadas = float(input("Ingresa el número de horas trabajadas: "))
precio_por_hora = float(input("Ingresa el precio por hora: "))
salario_bruto = horas_trabajadas * precio_por_hora
descuento = salario_bruto * 0.08
salario_neto = salario_bruto - descuento
print(f"Salario bruto: ${salario_bruto:.2f}")
print(f"Descuento del 8%: ${descuento:.2f}")
print(f"Salario neto: ${salario_neto:.2f}")
