tareas = []
opcion = ""

while opcion != "5":
    print("\n1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como hecha")
    print("4. Borrar tarea")
    print("5. Salir")

    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        tarea = input("Escribe la tarea: ")
        tareas.append([tarea, "pendiente"])
        print("Tarea añadida.")

    elif opcion == "2":
        if not tareas:
            print("No hay tareas.")
        else:
            for i in range(len(tareas)):
                print(f"{i + 1}. {tareas[i][0]} - {tareas[i][1]}")

    elif opcion == "3":
        for i in range(len(tareas)):
            print(f"{i + 1}. {tareas[i][0]} - {tareas[i][1]}")
        num = int(input("¿Qué tarea has terminado? (número): "))
        tareas[num - 1][1] = "hecha"
        print("Tarea marcada como hecha.")

    elif opcion == "4":
        for i in range(len(tareas)):
            print(f"{i + 1}. {tareas[i][0]} - {tareas[i][1]}")
        num = int(input("¿Qué tarea quieres borrar? (número): "))
        borrada = tareas.pop(num - 1)
        print(f"Tarea '{borrada}' borrada.")

    elif opcion == "5":
        print("Adiós")

    else:
        print("Opción no válida.")