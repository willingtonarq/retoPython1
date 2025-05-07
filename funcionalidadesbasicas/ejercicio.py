tareas = []


opciones = (
    "Añadir tarea",
    "Marcar tarea completada o pendiente",
    "Editar tarea",
    "Eliminar tarea",
    "Mostrar tareas",
    "Filtrar por estado",
    "Salir"
)

def mostrar_menu():
    print("\n--- MENÚ ---")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

def añadir_tarea():
    descripcion = input("Descripción: ")
    fecha = input("Fecha límite (YYYY-MM-DD): ")
    categoria = input("Categoría: ")
    tarea = {
        "descripcion": descripcion,
        "fecha_limite": fecha,
        "estado": "pendiente",
        "categoria": categoria
    }
    tareas.append(tarea)
    print("✅ Tarea añadida con éxito.")

def mostrar_tareas(filtro_estado=None):
    if not tareas:
        print("⚠️ No hay tareas registradas.")
        return

    for i, tarea in enumerate(tareas):
        if filtro_estado and tarea["estado"] != filtro_estado:
            continue
        print(f"{i}. {tarea['descripcion']} - {tarea['fecha_limite']} - {tarea['estado']} - {tarea['categoria']}")

def cambiar_estado():
    if not tareas:
        print("⚠️ No hay tareas para modificar.")
        return

    mostrar_tareas()
    try:
        i = int(input("Ingrese el número de la tarea: "))
        if i < 0 or i >= len(tareas):
            print("❌ Número inválido.")
            return
        nuevo_estado = input("Nuevo estado (pendiente/completada): ").strip().lower()
        if nuevo_estado not in ["pendiente", "completada"]:
            print("❌ Estado inválido.")
            return
        tareas[i]["estado"] = nuevo_estado
        print("✅ Estado actualizado.")
    except ValueError:
        print("❌ Por favor, ingrese un número válido.")

def editar_tarea():
    if not tareas:
        print("⚠️ No hay tareas para editar.")
        return

    mostrar_tareas()
    try:
        i = int(input("Número de la tarea a editar: "))
        if i < 0 or i >= len(tareas):
            print("❌ Número inválido.")
            return
        nueva_desc = input("Nueva descripción (enter para dejar igual): ")
        nueva_fecha = input("Nueva fecha límite (enter para dejar igual): ")

        if nueva_desc:
            tareas[i]["descripcion"] = nueva_desc
        if nueva_fecha:
            tareas[i]["fecha_limite"] = nueva_fecha

        print("✅ Tarea actualizada.")
    except ValueError:
        print("❌ Por favor, ingrese un número válido.")

def eliminar_tarea():
    if not tareas:
        print("⚠️ No hay tareas para eliminar.")
        return

    mostrar_tareas()
    try:
        i = int(input("Número de la tarea a eliminar: "))
        if i < 0 or i >= len(tareas):
            print("❌ Número inválido.")
            return
        tareas.pop(i)
        print("✅ Tarea eliminada.")
    except ValueError:
        print("❌ Por favor, ingrese un número válido.")

def filtrar_por_estado():
    if not tareas:
        print("⚠️ No hay tareas para filtrar.")
        return

    estado = input("Ingrese estado a mostrar (pendiente/completada): ").strip().lower()
    if estado not in ["pendiente", "completada"]:
        print("❌ Estado inválido.")
        return
    mostrar_tareas(filtro_estado=estado)

def programa():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            añadir_tarea()
        elif opcion == "2":
            cambiar_estado()
        elif opcion == "3":
            editar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            mostrar_tareas()
        elif opcion == "6":
            filtrar_por_estado()
        elif opcion == "7":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

programa()
