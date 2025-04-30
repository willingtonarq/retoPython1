''' Calcular la nómina semanal (salario neto) de un trabajador de una empresa cuyo 
trabajo se paga por horas. Leer por teclado el número de horas y el precio de la hora. 
El cálculo se realiza del siguiente modo: 
• Las primeras 35 horas se pagan a la tarifa normal. 
• Las horas extras se pagan un 25% más que las normales. 
• Los impuestos a deducir a los trabajadores varían en función de su sueldo mensual. 
• Si el sueldo es menor de 1000€, libre de impuestos. 
• Si el sueldo está entre 1000€ y 2000€, los impuestos son el 20%. 
• Si el sueldo es mayor de 2000€, el 30%. '''

numeroHoras = int(input("Ingresa el número de horas: "))

precioHora = 6189
tarifaNormal = precioHora
horasExtras = (precioHora * 0.25) + (precioHora)
