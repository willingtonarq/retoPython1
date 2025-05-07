#codificado por Esteban Cortes, Santiago loaiza y David Restrepo
def menu():
    print("1. Añadir tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("4. Modificar tarea")
    print("5. Filtro de tareas por estado")
    print("6. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion

def añadirtarea():
    print("Añadir tarea")
    tarea = input("Introduce la tarea: ")
    fecha = input("Introduce la fecha (DD/MM/AAAA): ")
    hora = input("Introduce la hora (HH:MM): ")
    estado = input("Diga estado de la tarea (pendiente/completada): ")  # Estado por defecto al añadir
    return (tarea, fecha, hora, estado)

def mostrartareas(tareas):
    print("Lista de tareas")
    if input("Quieres ver todas las tareas? (s/n): ").lower() == "s":
        for i, tarea in enumerate(tareas):
            print(f"{i + 1}. {tarea[0]} - Fecha: {tarea[1]}, Hora: {tarea[2]}, Estado: {tarea[3]}")
    if not tareas:
        print("No hay tareas disponibles.")
        return


def eliminartarea(tareas):
    print("Eliminar tarea")
    mostrartareas(tareas)
    indice = int(input("Selecciona el número de la tarea a eliminar: ")) - 1
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
        print("Tarea eliminada.")
    else:
        print("Índice inválido. No se eliminó ninguna tarea.")

def modificartarea(tareas):
    print("Modificar tarea")
    mostrartareas(tareas)
    indice = int(input("Selecciona el número de la tarea a modificar: ")) - 1
    if 0 <= indice < len(tareas):
        nueva_tarea = input("Introduce la nueva tarea: ")
        nueva_fecha = input("Introduce la nueva fecha (DD/MM/AAAA): ")
        nueva_hora = input("Introduce la nueva hora (HH:MM): ")
        nuevo_estado = input("Diga nuevo estado de la tarea (pendiente/completada): ")  # Nuevo estado
        tareas[indice] = (nueva_tarea, nueva_fecha, nueva_hora, nuevo_estado)
        print("Tarea modificada.")
    else:
        print("Índice inválido. No se modificó ninguna tarea.")
   

def filtrotareas(tareas):
    print("Filtro de tareas por estado")
    estado = input("Introduce el estado (pendiente/completada): ").lower()
    for i, tarea in enumerate(tareas):
        if tarea[3] == estado:
            print(f"{i + 1}. {tarea[0]} - Fecha: {tarea[1]}, Hora: {tarea[2]}, Estado: {tarea[3]}")
    if not any(t[3] == estado for t in tareas):
        print(f"No hay tareas con el estado '{estado}'.")


def Salir():
    print("Saliendo del programa...")
    exit()  

menu_opciones = {
    "1": añadirtarea,
    "2": mostrartareas,
    "3": eliminartarea,
    "4": modificartarea,
    "5": filtrotareas,
    "6": Salir
}

tareas = []
while True:
    opcion = menu()
    if opcion == "1":
        tarea = añadirtarea()
        tareas.append(tarea + ("pendiente",))  # Añadir estado por defecto
    elif opcion == "2":
        mostrartareas(tareas)
    elif opcion == "3":
        eliminartarea(tareas)
    elif opcion == "4":
        modificartarea(tareas)
    elif opcion == "5":
        filtrotareas(tareas)
    elif opcion == "6":
        Salir()
    else:
        print("Opción inválida. Intenta de nuevo.")