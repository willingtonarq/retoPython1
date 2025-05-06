

# n = int(input("Ingrese una cantidad de valores elementos: "))

# if n <= 0:
#     print("Debe ingresar un numero entero positivo") 

# else:
#     lista = []
#     for i in range(n):
#       numero = float(input(f"Ingrese el elemento {i + 1}: "))  
#       lista.append(numero)

#     producto = 1
#     for elemento in lista:
#        producto *= elemento

#        print("\nLa lista ingresada es: " , lista)
#        print("El prodcuto de todos los elementos es: " , producto)

# n = int(input("Ingrese una cantidad de valores elementos: "))

# if n <= 0:
#     print("Debe ingresar un numero entero positivo") 

# else:
#     lista = []
#     for i in range(n):
#       numero = float(input(f"Ingrese el elemento {i + 1}: "))  
#       lista.append(numero)

#     suma = 1
#     for elemento in lista:
#        suma += elemento

#        print("\nLa lista ingresada es: " , lista)
#        print("El prodcuto de todos los elementos es: " , suma)

# n = int(input("Ingrese la cantidad de elementos en la lista: "))
# lista = []

# for i in range(n):
#     numero = float(input(f"Ingrese el elemento {i + 1}: "))
#     lista.append(numero)

# x = float(input("\nIngrese el valor X para comparar: "))

# mayores = []

# for numero in lista:
#     if numero > x:
#         mayores.append(numero)

# print(f"\nSe encontraron {len(mayores)} elementos mayores que {x}.")
# print("Elementos mayores:", mayores)

# n = int(input("Ingrese la cantidad de elementos en la lista: "))
# lista = []

# for i in range(n):
#     numero = float(input(f"Ingrese el elemento {i + 1}: "))
#     lista.append(numero)

# suma_impares = 0
# for i in range(1, len(lista), 2): 
#     suma_impares += lista[i]

# print("\nLa lista ingresada es:", lista)
# print("La suma de los elementos en posiciones impares es:", suma_impares)

# n = int(input("Ingrese la cantidad de elementos en la lista: "))
# lista = []

# for i in range(n):
#     numero = float(input(f"Ingrese el elemento {i + 1}: "))
#     lista.append(numero)

# positivos = 0
# negativos = 0
# ceros = 0

# for numero in lista:
#     if numero > 0:
#         positivos += 1
#     elif numero < 0:
#         negativos += 1
#     else:
#         ceros += 1

# print("\nLista ingresada:", lista)
# print(f"Positivos: {positivos}")
# print(f"Negativos: {negativos}")
# print(f"Ceros: {ceros}")

# n = int(input("Ingrese la cantidad de elementos en la lista: "))
# lista = []

# for i in range(n):
#     numero = float(input(f"Ingrese el elemento {i + 1}: "))
#     lista.append(numero)

# cuadrados = []
# for numero in lista:
#     cuadrados.append(numero ** 2)

# print("\nLista original:", lista)
# print("Cuadrados de los elementos:", cuadrados)

# n = int(input("Ingrese la cantidad de elementos en la lista: "))
# lista = []

# for i in range(n):
#     numero = float(input(f"Ingrese el elemento {i + 1}: "))
#     lista.append(numero)

# x = float(input("\nIngrese el número X que desea buscar: "))

# cantidad = lista.count(x)

# if cantidad == 0:
#     print(f"\nEl número {x} no se encuentra en la lista.")
# elif cantidad == 1:
#     print(f"\nEl número {x} aparece una sola vez en la lista.")
# else:
#     print(f"\nEl número {x} se encuentra repetido {cantidad} veces en la lista.")


# n = int(input("Ingrese la cantidad de elementos en la lista: "))
# lista = []

# for i in range(n):
#     numero = float(input(f"Ingrese el elemento {i + 1}: "))
#     lista.append(numero)

# x = float(input("\nIngrese el valor X para comparar: "))

# posiciones = []

# for i in range(len(lista)):
#     if lista[i] < x:
#         posiciones.append(i)

# if posiciones:
#     print(f"\nElementos menores a {x} encontrados en las siguientes posiciones:")
#     for pos in posiciones:
#         print(f"Posición {pos} → Valor: {lista[pos]}")
# else:
#     print(f"\nNo se encontraron elementos menores a {x}.")






