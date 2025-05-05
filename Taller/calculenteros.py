#Implementar  un  algoritmo  que  calcule  el  producto  de  dos  números  enteros  (n*m) 
#haciendo sólo sumas.


#for
n = int(input("Ingresa un número: "))
m = int(input("Ingresa otro número: "))
producto = 0
for i in range(m):
    producto += n
print("El producto de", n, "y", m, "es:", producto)


""" # #while
n = int(input("Ingresa un número: "))
m = int(input("Ingresa otro número: "))
producto = 0
i = 0
while i < m:
    producto += n
    i += 1
print("El producto de", n, "y", m, "es:", producto)
 """




