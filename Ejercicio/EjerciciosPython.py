nombre = str(input("¿Cual es tu nombre? \n Nombre: "))
edad = str(input("¿Cuantos años tienes? \n Edad: "))
print("Hola " + nombre + ", bienvenido. Tienes " + edad + " años")

opcion = 99
while opcion != 0:
    print("1. Area de un triangulo \n2. Area de un circulo \n3. Kg a libras \n4. Descuentos en productos \n5. Nota final \n6. ((A + B)**2)/3 \n7. Días a segundos \n8. Producto, suma y promedio de 4 numeros \n9. Salario")
    print("0. Salir")
    opcion = int(input("Ingrese la opción deseada: "))


    if opcion == 1:
        # Area de un triangulo9
        base = float(input("Ingrese la base del triangulo. \n Base: "))
        altura = float(input("Ingrese la altura del triangulo \ n Altura: "))
        area = (base * altura) / 2
        print("El area del triangulo es: " + str(area))

    elif opcion == 2:
        # Area de un circulo
        areaCirculo = float(input("Ingrese el area del circulo \n Area: "))
        radio = (areaCirculo**2 / 3.14)
        print("El radio del circulo es: " + str(radio))

    elif opcion == 3:
        # Kg a libras
        PesoKg = float(input("Ingrese el peso en kg \n Peso: "))
        PesoLibras = PesoKg * 2.20462
        print("El peso en libras es: " + str(PesoLibras) + " libras")

    elif opcion == 4:
        # Descuentos en productos
        precio = float(input("Ingrese el precio del producto \n Precio: "))
        precioDescuento = precio * 0.10
        print("El precio con descuento es: " + str(precioDescuento) + " pesos")

    elif opcion == 5:
        # Nota final
        nota1= (float(input("Ingrese la nota 1: ")))*0.30
        nota2= (float(input("Ingrese la nota 2: ")))*0.30
        nota3= (float(input("Ingrese la nota 3: ")))*0.25
        nota4= (float(input("Ingrese la nota 4: ")))*0.15
        notaFinal= nota1 + nota2 + nota3 + nota4
        print("La nota final es: " + str(notaFinal))

    elif opcion == 6:
        # ((A + B)**2)/3
        daroA = float(input("Ingrese el valor de A: "))
        daroB = float(input("Ingrese el valor de B: "))
        resultado = ((daroA + daroB) ** 2) / 3
        print("El resultado es: " + str(resultado))

    elif opcion == 7:
        # Días a segundos
        dias = float(input("Ingrese la cantidad de días: "))
        segundos = dias * 86400  # 1 día = 86400 segundos
        print("La cantidad de segundos es: " + str(segundos))

    elif opcion == 8:
        # producto, suma y promedio de 4 numeros
        valor1 = float(input("Ingrese el valor 1: "))
        valor2 = float(input("Ingrese el valor 2: "))   
        valor3 = float(input("Ingrese el valor 3: "))
        valor4 = float(input("Ingrese el valor 4: "))
        producto = valor1 * valor2 * valor3 * valor4
        suma = valor1 + valor2 + valor3 + valor4
        promedio = suma / 4
        print("El producto es: " + str(producto) + "\n La suma es: " + str(suma) + "\n El promedio es: " + str(promedio))

    elif opcion == 9:
        # Salario
        horasTrabajadas = float(input("Ingrese las horas trabajadas: "))
        pagoHora = float(input("Ingrese el pago por hora: "))
        sueldo = horasTrabajadas * pagoHora
        sueldoNeto = sueldo - (sueldo * 0.8)  # Descuento del 8%
        print("El sueldo neto es: " + str(sueldoNeto))
        
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")
        
print("Gracias por usar el programa. ¡Hasta luego!")
# Fin del programa