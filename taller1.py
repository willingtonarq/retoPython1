"""
ejercicio #1

edad = int(input("introduce tu edad ")) 
peso = int(input("introduce tu peso")) 

print ("la edad tuya es", edad," y tu peso es", peso) 
 """
 
 
 
""" #ejercicio #2   
base = int(input("ingrese la base del traingulo "))
altura = int(input("ingrese la altura del triangulo"))

print ("el area del triangulo es :",(base*altura)/2) """





"""
#ejercicio #3

radio = int(input("ingrese el radio del circulo "))
pi = 3.14
area = pi*(radio**2)

print ("el area del circulo es : ", area)
 """
 
"""  #ejercicio #4
peso = int(input("ingrese su peso en kilogramos "))

print("su peso en libras es : ", peso*2.20462) """


""" 
#ejercicio #5
precio = int (input("hola ingrese el precio para calcular el descuento")) 
descuento = int(input("ingrese el porcentaje de descuento"))
precio_final = precio - (precio *(descuento /100))
print ("el precio final es : ", precio_final)
  """
  
  
""" #ejercicio #6
nota1 = int(input("ingrese la primera nota "))
nota2 = int(input("ingrese la segunda nota "))
nota3 = int(input("ingrese la tercera nota "))
nota4 = int(input("ingrese la cuarta nota "))

promedio = (nota1-(nota1*0.3) + nota2-(nota2*0.3) + nota3-(nota3*0.25) + nota4-(nota4*0.15)) / 4
print ("el promedio es : ", promedio) """

""" #ejercicio #7

A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))

resultado = ((A + B) ** 2) / 3

print("El resultado  es:", resultado)
 """
 
""" #ejercicio #8
dias = int(input("Ingrese el número de días: "))

segundos = dias * 24 * 60 * 60

print(f"El número de segundos en {dias} días es: {segundos}") """


""" #ejecicio #9

n1 = int(input("ingrese el primer numero "))
n2 = int(input("ingrese el segundo numero "))
n3 = int(input("ingrese el tercer numero "))
n4 = int(input("ingrese el cuarto numero "))

print (f"el producto de los cuatro numeros es : {n1*n2*n3*n4} \n la suma de estos mismos es de :{n1+n2+n3+n4} \n el promedio de los cuatro numeros es {(n1+n2+n3+n4)/4}") 
  """
""" #ejercicio #10

# Solicitar datos al usuario
horas_trabajadas = int(input("Ingrese el número de horas trabajadas: "))
precio_hora = int(input("Ingrese el precio de la hora: "))

# Calcular el salario bruto
salario_bruto = horas_trabajadas * precio_hora

# Calcular el descuento del 8%
descuento = salario_bruto * 0.08

# Calcular el salario neto
salario_neto = salario_bruto - descuento

# Imprimir el resultado
print(f"El salario neto del trabajador es: {salario_neto}") """