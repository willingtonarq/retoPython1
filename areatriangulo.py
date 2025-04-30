#Escribir un programa que calcule el área de un triángulo recibiendo como entrada el valor de base y altura. Área= base*altura/e en python
#Ejemplo de entrada: base=5, altura=10
#Ejemplo de salida: El área del triángulo es: 25.0


# función para calcular el área del triángulo
def area_triangulo(base, altura):
    return (base * altura) / 2

# función principal
def main():
    # entrada de datos
    base = float(input("Introduce la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))

    # cálculo del área
    area = area_triangulo(base, altura)

    # salida de resultados
    print(f"El área del triángulo es: {area}")


# llamada a la función principal
if __name__ == "__main__":
    main()
