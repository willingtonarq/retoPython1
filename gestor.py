tareas=[]
def añadir_tareas(tarea):
    tareas.append(tarea)
    print("Tarea añadida con éxito.")
def eliminar_tareas(nombre_eliminar):
    cont=True
    for tarea in tareas:
        if tarea["nombre"] == nombre_eliminar:
            tareas.remove(tarea)
            print("Tarea eliminada con éxito.")
            cont=False
            return
    if cont:
        print("La tarea no se encuentra en la lista.")
def mostrar_tareas():
    if tareas:
        print("Tareas:")
        for tarea in tareas:
            print(tarea)
    else:
        print("No hay tareas en la lista.")
def editar_tarea(nombre_editar, nueva_tarea):
    for i, tarea in enumerate(tareas):
        if tarea["nombre"] == nombre_editar:
            tareas[i] = nueva_tarea
            print("Tarea editada con éxito.")
            return
    print("La tarea no se encuentra en la lista.")
def filtrar_tareas(estado):
    cont=False
    for tarea in tareas:
        if tarea["estado"] == estado:
            print(tarea)
            cont=True
    if not cont:
        print("No hay tareas con el estado especificado.")
def editar_estado_tarea(nombre_editar, nuevo_eatado):
    cont=True
    for i, tarea in enumerate(tareas):
        if tarea["nombre"] == nombre_editar:
            tareas[i]["estado"] = nuevo_eatado
            print("Estado de la tarea editado con éxito.")
            cont=False
            return
    if cont:
        print("La tarea no se encuentra en la lista.")
def main():
    while True:
        print("1. Añadir tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar tareas")
        print("4. Editar tarea")
        print("5. Filtrar tareas")
        print("6. editar estado de tarea")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            fecha = input("Ingrese la fecha de la tarea (YYYY-MM-DD): ")
            estado = input("Ingrese el estado de la tarea: ")
            tarea = {
                "nombre": nombre,
                "descripcion": descripcion,
                "fecha": fecha,
                "estado": estado
            }
            añadir_tareas(tarea)
        elif opcion == "2":
            nombre_eliminar=input("Ingrese el nombre de la tarea a eliminar: ")
            eliminar_tareas(nombre_eliminar)
        elif opcion == "3":
            mostrar_tareas()
        elif opcion == "4":
            nombre_editar = input("Ingrese el nombre de la tarea a editar: ")
            nombre = input("Ingrese el nombre de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            fecha = input("Ingrese la fecha de la tarea (YYYY-MM-DD): ")
            estado = input("Ingrese el estado de la tarea: ")
            nueva_tarea = {
                "nombre": nombre,
                "descripcion": descripcion,
                "fecha": fecha,
                "estado": estado
            }
            editar_tarea(nombre_editar, nueva_tarea)
        elif opcion == "5":
            estado = input("Ingrese el estado de las tareas a filtrar: ")
            filtrar_tareas(estado)
        elif opcion == "6":
            nombre_editar = input("Ingrese el nombre de la tarea a editar: ")
            nuevo_estado = input("Ingrese el nuevo estado de la tarea: ")
            editar_estado_tarea(nombre_editar, nuevo_estado)
        elif opcion == "7":
            break
        else:
            print("Opción no válida.")
if __name__ == "__main__":
    main()