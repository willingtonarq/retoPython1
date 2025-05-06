# # contador= 0
# # n = int(input("ingrese el numero 1: "))
# # for  i in range(1, n + 1) :
# #     contador += i
# # print(" la suma es ", contador)
#------------------------------------------------------------------------------------------------
# i = 1
# while  i <= n:
#   contador += i
#   i += 1
# print("tu suma es ", contador)
#------------------------------------------------------------------------------------------------
# numero 2
# suma = 0
# i = 1
# n = int(input("ingresa un numero natural"))
# for i in range ( 1, n + 1, i):3
#     i = i **2
#     suma += i
# print(suma)  
#------------------------------------------------------------------------------------------------
# while  i < n :
#     i = i **2
#     suma += i
# print(suma)  
#------------------------------------------------------------------------------------------------
# contador= 0
# n = int(input("ingrese el numero 1: "))
# m = int(input("ingrese el numero 2: "))

# # for  i in range(n, m  + 1) :
# #     contador += i
# # print(" la suma es ", contador)
# #------------------------------------------------------------------------------------------------
# i = n
# while i < m :
#    contador += i
#    i += 1
# print(" la suma es ", contador)
# #------------------------------------------------------------------------------------------------
# contador = 0
# n = int(input("ingresa un numero "))
# m = int (input("ingresa un numero"))
# for i in range(m):
#     contador += n
# print(contador)
# # #------------------------------------------------------------------------------------------------
# suma = 0
# i = 0
# while i < m :
#     suma += n
#     i += 1
# print(suma)
#------------------------------------------------------------------------------------------------
# contador = 0
# for i in range(5):
#  n = int(input(f"Ingrese el número {i + 1}: "))
#  contador +=n
# promedio = contador / 5
# print(promedio) 
#------------------------------------------------------------------------------------------------
# i = 0
# suma = 0
# while i < 5 :
#  s = int(input(f"ingresa un numero {i +1}"))
#  suma += s
#  i += 1
# # promedio = s / 5
# # print(s)

# # Dada las horas Extras trabajadas de una persona por día en una semana, de lunes a viernes,
# # y la tarifa de pago. Calcular el valor total a pagar e imprimirlo por pantalla.
# valor = 0  

# for i in range(5):
#     hora = float(input(f"Horas extras del día {i + 1}: "))
#     valor += hora  

# tarifa1 = float(input("Ingrese la tarifa por hora: "))
# tarifa = valor * tarifa1  

# print(f"Total de horas trabajadas: {valor}")
# print(f"Tarifa por hora: {tarifa1}")
# print(f"Total a pagar: {tarifa}")
# #------------------------------------------------------------------------------------------------
# i = 0
# horas = 0

# while i < 5:
#     horas += float(input(f"Horas extras del día {i + 1}: "))
#     i += 1

# tarifa = float(input("Tarifa por hora: "))
# total = horas * tarifa

# print("Total a pagar:", total)

#------------------------------------------------------------------------------------------------

# suma = 0
# multi = 1

# for i in range(20, 400 + 1):  
#     if i % 2 == 0:
#         suma += i
#         multi *= i

# print("Suma de pares:", suma)
# print("Producto de pares:", multi)
# #------------------------------------------------------------------------------------------------
# i = 20
# suma = 0
# producto = 1

# while i <= 400:
#     if i % 2 == 0:
#         suma += i
#         producto *= i
#     i += 1

# print( suma)
# print( producto)
#------------------------------------------------------------------------------------------------
# suma = 0
# producto = 1

# for i in range(20, 401):  # 401 para incluir el 400
#     if i % 2 == 0:
#         suma += i
#         producto *= i

# print( suma)
# print( producto)
# #------------------------------------------------------------------------------------------------

# i = 20
# suma = 0
# producto = 1

# while i <= 400:
#     if i % 2 == 0:
#         suma += i
#         producto *= i
#     i += 1

# print( suma)
# print( producto)
# #------------------------------------------------------------------------------------------------
# numeroSecreto = 2

# for i in range(3):
#     m = int(input("Ingrese un número: "))
#     if numeroSecreto == m:
#         print("¡Adivinaste!")
#         break
# else:
#     print("Fallaste tus intentos.")
#------------------------------------------------------------------------------------------------

# numeroSecreto = 2
# intentos = 0

# while intentos < 3:
#     m = int(input("Ingresa un número: "))
#     if numeroSecreto == m:
#         print("¡Adivinaste!")
#         break
#     intentos += 1

# if intentos == 3:
#     print("Fallaste tus intentos.")
# #------------------------------------------------------------------------------------------------
# suma = 0
# contador = 0

# while True:
#     num = int(input("Ingresa un número positivo: "))
#     if num <= 0:
#         break
#     suma += num
#     contador += 1

# print("Suma:", suma)
# if contador > 0:
#     print("Promedio:", suma / contador)

# # #------------------------------------------------------------------------------------------------



# suma = 0
# contador = 0

# for _ in range(100): 
#     num = int(input("Ingresa un número positivo: "))
#     if num <= 0:
#         break
#     suma += num
#     contador += 1

# print("Suma:", suma)
# if contador > 0:
#     print("Promedio:", suma / contador)

# #------------------------------------------------------------------------------------------------







# n = int(input("Ingresa un número: "))

# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)

# #------------------------------------------------------------------------------------------------

# n = int(input("Ingresa un número: "))
# i = 1
# while i <= 10:
#     print(n, "x", i, "=", n * i)
#     i += 1


   
