def validarTarea(categoria):
    if categoria == "Estudio":
        return True
    elif categoria == "Casa":
        return True
    elif categoria == "Personal":
        return True
    elif categoria == "Otros":
        return True
    else:
        print("Elija una de las categorias permitidas")
        return False
    
def imprimirTareas():
    i = 0
    if tareas == []:
        return print("No hay tareas")
    for valor in tareas:
        i += 1
        print(f"{i}- Titulo: {valor.get("Titulo")} | Estado: {valor.get("Estado")}")

def opcionEditar(opcion, numeroTarea):
    if opcion == 1:
        print("Titulo:",tareas[numeroTarea-1].get("Titulo"))
        tituloTarea = input("Ingrese el titulo nuevo: ")
        tareas[numeroTarea-1].update({'Titulo':tituloTarea})
    elif opcion == 2:
        print("Descripcion:",tareas[numeroTarea-1].get("Descripcion"))
        descripcionTarea = input("Ingrese la descripcion nueva: ")
        tareas[numeroTarea-1].update({'Descripcion':descripcionTarea})
    elif opcion == 3:
        print("Fecha limite:",tareas[numeroTarea-1].get("Fecha limite"))
        fechaTarea = input("Ingrese la fecha de entrega nueva: ")
        tareas[numeroTarea-1].update({'Fecha limite':fechaTarea})
    elif opcion == 4:
        print("Categoria:",tareas[numeroTarea-1].get("Categoria"))
        validar = False
        while (validar == False):
             categoria = input("Ingrese la categoria nueva: Estudio, Casa, Personal, Otros: ")
             validar = validarTarea(categoria)
        tareas[numeroTarea-1].update({'Categoria':categoria})
    elif opcion == 0:
        print("Edición terminada")
    else:
        print("Opcion no valida")

def  opcionEditarEstado(opcion, numeroTarea):
    if opcion == 1:
        tareas[numeroTarea-1].update({'Estado':'Pendiente'})
    elif opcion == 2:
        tareas[numeroTarea-1].update({'Estado':'En proceso'})
    elif opcion == 3:
        tareas[numeroTarea-1].update({'Estado':'Terminado'})
    elif opcion == 0:
        print("Estado actualizado")
    else:
        print("Opcion no valida")

def imprimirPorEstado(opcion):
    i = 0
    if opcion == 1:
        for valor in tareas:
            if valor.get("Estado") == "Pendiente":
                i += 1
                print(f"{i}- {valor}")
    elif opcion == 2:
        for valor in tareas:
            if valor.get("Estado") == "En proceso":
                i += 1
                print(f"{i}- {valor}")
    elif opcion == 3:
        for valor in tareas:
            if valor.get("Estado") == "Terminado":
                i += 1
                print(f"{i}- {valor}")
    elif opcion == 0:
        print("Saliendo")
    else:
        print("Opcion no valida")

def imprimirPorCategoria(opcion):
    i = 0
    if opcion == 1:
        for valor in tareas:
            if valor.get("Categoria") == "Estudio":
                i += 1
                print(f"{i}- {valor}")
    elif opcion == 2:
        for valor in tareas:
            if valor.get("Categoria") == "Casa":
                i += 1
                print(f"{i}- {valor}")
    elif opcion == 3:
        for valor in tareas:
            if valor.get("Categoria") == "Personal":
                i += 1
                print(f"{i}- {valor}")
    elif opcion == 4:
        for valor in tareas:
            if valor.get("Categoria") == "Otros":
                i += 1
                print(f"{i}- {valor}")
    elif opcion == 0:
        print("Saliendo")
    else:
        print("Opcion no valida")

def opcionImprimirTareas(opcion):
    if tareas == []:
        return print("No hay tareas")
    
    if opcion == 1:
        imprimirTareas()
    elif opcion == 2:
        print("Mostrar por estado")
        opcion2 = 1
        while opcion2 != 0:
            opcion2 = int(input(menu5))
            imprimirPorEstado(opcion2)
    elif opcion == 3:
        print("Mostrar por categoria")
        opcion2 = 1
        while opcion2 != 0:
            opcion2 = int(input(menu6))
            imprimirPorCategoria(opcion2)   
    elif opcion == 0:
        print("Saliendo")
    else:
        print("Opcion no valida") 

def seleccionarOpcion(opcion):
    if opcion == 1:
        print("Añadir tarea")
        tituloTarea = input("Ingrese el titulo de la tarea: ")
        descripcionTarea = input("Ingrese la descripcion de la tarea: ")
        fechaTarea = input("Ingrese la fecha de entrega de la tarea: ")
        
        validar = False
        while (validar == False):
             categoria = input("Ingrese la categoria de la tarea: Estudio, Casa, Personal, Otros: ")
             validar = validarTarea(categoria) 

        tarea = {"Titulo": tituloTarea,
                 "Descripcion": descripcionTarea,
                 "Fecha limite": fechaTarea,
                 "Estado": "Pendiente",
                 "Categoria": categoria}
        tareas.append(tarea)
    elif opcion == 2:
        print("Editar tarea")
        imprimirTareas()
        numeroTarea = int(input("Ingrese el numero de la tarea a editar: "))
        opcion2 = 1
        while opcion2 != 0:
            opcion2 = int(input(menu2))
            opcionEditar(opcion2, numeroTarea)
    elif opcion == 3:
        print("Marcar tarea")
        imprimirTareas()
        numeroTarea = int(input("Ingrese el numero de la tarea a marcar: "))
        opcion2 = 1
        while opcion2 != 0:
            opcion2 = int(input(menu3))
            opcionEditarEstado(opcion2, numeroTarea)
    elif opcion == 4:
        print("Eliminar tarea")
        imprimirTareas()
        numeroTarea = int(input("Ingrese el numero de la tarea a eliminar: "))
        print(tareas.pop(numeroTarea-1))
    elif opcion == 5:
        print("Mostrar lista de tareas")
        opcion2 = 1
        while opcion2 != 0:
            opcion2 = int(input(menu4))
            opcionImprimirTareas(opcion2)
    elif opcion == 0:
        print("Saliendo...")
    else:
        print("Opcion no valida")

menu = """Elija una opcion:
1) Añadir tarea
2) Editar tarea
3) Marcar tarea
4) Eliminar tarea
5) Mostrar lista de tareas
0) Salir
"""

menu2 = """Elija una opcion
1) Editar titulo
2) Editar descripción
3) Editar fecha
4) Editar categoria
0) Salir
"""

menu3 = """Marcar como
1) Pendiente
2) En proceso
3) Terminado
0) Salir
"""

menu4 = """Elije una opcion
1) Mostrar todas las tareas
2) Mostrar por estado
3) Mostrar por categoria
0) salir
"""

menu5 = """Elije una opcion
1) Pendiente
2) En proceso
3) Terminado
0) Salir
"""

menu6 = """Elije una opcion
1) Estudio
2) Casa
3) Personal
4) Otros
0) Salir
"""

opcion = 1
tareas = []
contador = 1
while(opcion != 0):
    print(menu)
    opcion = int(input(menu))
    seleccionarOpcion(opcion)