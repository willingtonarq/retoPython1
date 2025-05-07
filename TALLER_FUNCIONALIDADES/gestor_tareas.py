"""Interfaz iteractiva a traves de la consola, donde el usuario puede ingresar comandos para gestionar las tareas"""
#FUNCIONES BASICAS
"""Añadir nuevas tareas con descripcion y fecha limite"""
"""Marcar tareas como completadas o pendientes"""
"""Editar la descripcion o fecha limite de una tarea"""
"""Eliminar tareas"""
"""Mostrar la lista de las tareas, filtrando por estado (completadas o pendientes), o por categoria"""

import datetime

# Lista para almacenar las tareas
tareas = []

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\n ----- Menú de Tareas -----")
    print("1. Añadir tarea.")
    print("2. Cambiar estado.")
    print("3. Editar tarea.")
    print("4. Eliminar tarea.")
    print("5. Mostrar tareas.")
    print("6. Salir.")

# Función añadir nueva tarea
def añadir_tarea():
    descripcion = input("Ingrese la descripción de la tarea: ")
    categoria = input("Ingrese la categoría de la tarea: ")
    fecha_limite = input("Ingrese la fecha límite (YYYY-MM-DD): ")

    # Validar la fecha límite
    try:
        fecha_limite = datetime.datetime.strptime(fecha_limite, "%Y-%m-%d").date()
        tarea = {
            "descripcion": descripcion,
            "categoria": categoria,
            "fecha_limite": fecha_limite,
            "completada": False
        }
        tareas.append(tarea)
        print("Tarea añadida con éxito.")
    except ValueError:
        print("Fecha inválida. Por favor, use el formato YYYY-MM-DD.")

# Funcion mostrar tarea
def mostrar_tareas():
    print("\n Filtrar por: ")
    print("1. Todas")
    print("2. Completadas")
    print("3. Pendientes")
    print("4. Por categoría")

    opcion = input("Elige una opcion: ")
    if  opcion == "1" :
        filtradas = tareas
    elif opcion == "2":
        filtradas = [tarea for tarea in tareas if tarea["completada"]]
    elif opcion == "3":
        filtradas = [tarea for tarea in tareas if not tarea["completada"]]
    elif opcion == "4":
        categoria = input("Ingrese la categoría de la tarea: ")
        filtradas = [tarea for tarea in tareas if tarea["categoria"] == categoria]
    else:
        print("Opción inválida.")
        return
    
    if not filtradas:
        print("No hay tareas que coincidan.")
        return
    else:
        print("Tareas:")
        for i, tarea in enumerate(filtradas, start=1):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i}. {tarea['descripcion']} - Fecha límite: {tarea['fecha_limite']} - Estado: {estado}")

# Funcion cambiar estado tarea
def cambiar_estado_tarea():
    mostrar_tareas()
    try:
        indice = int(input("Ingrese el número de la tarea a la que le desea cambiar el estado: ")) - 1
        if 0 <= indice < len(tareas):
            tareas[indice]["completada"] = not tareas[indice]["completada"]
            estado = "completada" if tareas[indice]["completada"] else "pendiente"
            print(f"Tarea '{tareas[indice]['descripcion']}' marcada como {estado}.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")

# Funcion editar tarea
def editar_tarea():
    mostrar_tareas()
    try:
        indice = int(input("Ingrese el número de la tarea a editar: ")) - 1
        if 0 <= indice < len(tareas):
            nueva_descripcion = input("Ingrese la nueva descripción de la tarea: ")
            nueva_categoria = input("Ingrese la nueva categoría de la tarea: ")
            nueva_fecha_limite = input("Ingrese la nueva fecha límite (YYYY-MM-DD): ")

            # Validar la fecha límite
            try:
                nueva_fecha_limite = datetime.datetime.strptime(nueva_fecha_limite, "%Y-%m-%d").date()
                tareas[indice]["descripcion"] = nueva_descripcion
                tareas[indice]["categoria"] = nueva_categoria
                tareas[indice]["fecha_limite"] = nueva_fecha_limite
                print("Tarea editada con éxito.")
            except ValueError:
                print("Fecha inválida. Por favor, use el formato YYYY-MM-DD.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")

# Funcion eliminar tarea
def eliminar_tarea():
    mostrar_tareas()
    try:
        indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tareas.pop(indice)
            print("Tarea eliminada con éxito.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")
    if opcion == "1":
        añadir_tarea()
    elif opcion == "2":
        cambiar_estado_tarea()
    elif opcion == "3":
        editar_tarea()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        mostrar_tareas()
    elif opcion == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida.")
