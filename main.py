import math

print('Ejercicio 1')

def ep(a, b):
    return (a, b)

a = int(input('Enter age: '))
b = int(input('Enter weight: '))

print(f'age is {a} and {b} is weight')


print('Ejercicio 2')
def triangle(b, h):
    return (b*h/2)

b = int(input('Enter the base: '))
h = int(input('Enter the height: '))

print(f'this is the answer {triangle(b,h)} ')


print('Ejercicio 3')

def radius(r):    
    return(r*r*math.pi)
r=int(input('Enter the radius: '))
print(f'this is the Area of this Circle{radius(r)}')


print('Ejercicio 4')
def weightkg(w):
    return(w*2.2046)
w=int(input('Enter your weight:'))
print(f'This is your weight in pound weight: {weightkg(w)}')

print('Ejercicio 5')
def discount(d):
    return(d*0.1)
d=int(input('Enter the price of the product: '))
print(f'this is the discount of this purchase: {discount(d)} the price of the product is {d} and the total price is {d-discount(d)}')

print('Ejercicio 6')
def notes(a,b,c,d):
    return(a*0.3 +b*0.3 +c*0.25 +d*0.15)
a=float(input('Enter the first note: '))
b=float(input('Enter the second note: '))
c=float(input('Enter the third note: '))
d=float(input('Enter the fourth note: '))
print(f'this is your final note: {notes(a,b,c,d)}')

print('Ejercicio 7')
def exp(a,b):
    return(a*a+b*b/3)
a=int(input('Enter the first number: '))
b=int(input('Enter the second number: '))
print(f'this is the result of the expression: {exp(a,b)}')

print('Ejercicio 8')
def daysec(d):
    return(d*86400)
d=int(input('Enter the number of days: '))
print(f'this is the number of days {d} and this is transpass in seconds {daysec(d)}')

print ('Ejercicio 9')
def values(a,b,c,d):
    return(a+b+c+d)
a=float(input('Enter the first number: '))
b=float(input('Enter the second number: '))
c=float(input('Enter the third number: '))
d=float(input('Enter the fourth number: '))
print(f'this is the plus: {values(a,b,c,d)},this is the product {a*b*c*d}  and this is the promedium {values(a,b,c,d)/4} ')

print('Ejercicio 10')
def salary(h,s):
    return(h*s)
h=int(input('Enter the number of hours: '))
s=int(input('Enter the price of hour: '))
print(f'this is the discount of salary: {salary(h,s)*0.08} and this is the total salary: {salary(h,s)-salary(h,s)*0.08}')

print('conditionals')
a=int(input('enter first number: '))

if a%2 == 0:
    print('number is pair')
else:
    print('number is odd')

print('Ejercicio 2')
b=int(input('Enter a number'))
if b>=0:
    print('is positive')
else:
    print('is negative')

print('Ejercicio 3')

temp=int(input('Enter the temperature'))
if temp <0:
    print('state Solid object')
elif temp <100:
    print('state liquid object')
elif temp>100:
    print('is gas')


print('Ejercicio 4')
def bisiesto(a):
    if (a % 4 == 0 and a % 100 != 0 or (a % 400 == 0)):
        print("es bisiesto")
    else:
        print("no es bisiesto")

print('Ejercicio 5')
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