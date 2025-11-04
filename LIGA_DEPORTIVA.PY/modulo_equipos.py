from funciones_basicas import generar_id



def crear_equipo(equipos):
    print("\n Creacion de Equipo")

    id_equipo = generar_id(equipos)
    print(f"ID {id_equipo} asignado automaticamente.")
    nombre_equipo = (input("Dime el nombre del equipo:"))
    ciudad = (input(f"Dime la ciudad a la que pertenece el equipo {nombre_equipo}:"))

    nuevo_equipo = {
        "id": id_equipo,
        "nombre": nombre_equipo,
        "ciudad": ciudad,
        "activo": True
    }

    equipos.append(nuevo_equipo)
    print(f"El equipo {nombre_equipo} ha sido creado correctamente con el id {id_equipo}")

def listar_equipos(equipos):
    for equipo in equipos:
        if equipo['activo']:
            print(f"ID: {equipo['id']} | Nombre: {equipo['nombre']} | Ciudad: {equipo['ciudad']} | Estado: {'activo' if equipo['activo'] else 'Inactivo'}")


def buscar_equipo(equipos):
    busqueda = int(input("Dime el id del equipo que quieres buscar:"))
    for equipo in equipos:
        if equipo['id'] == busqueda:
            print("\nArtículo encontrado:")
            print("ID:", equipo["id"])
            print("Nombre:", equipo["nombre"])
            print("Ciudad:", equipo["ciudad"])
            print("Estado:", "activo" if equipo["activo"] else "Inactivo")
            return
        else:
            print("No se encontró un equipo con ese ID.")

def actualizar_datos(equipos):
    actualizar = int(input("Dime el id del equipo que quieres actualizar:"))
    for equipo in equipos:
        if equipo['id'] == actualizar:
            nuevo_nombre = (input("Dime el nuevo nombre que le quieres agregar (deja en blanco para no cambiar):"))
            if nuevo_nombre != "":
                equipo['nombre'] = nuevo_nombre
            
            nueva_ciudad = (input("Dime la nueva ciudad que le quieres agregar (deja en blanco para no cambiar):"))
            if nueva_ciudad != "":
                equipo['ciudad'] = nueva_ciudad

            print("Artículo actualizado correctamente.\n")
            return
        
        else:
            print("No se ha encontrado ningun equipo con ese ID")
    
def eliminar_equipo(equipos):
    busqueda = input("Dime el id del equipo que quieres eliminar (convertir estado a inactivo): ")

    for equipo in equipos:
        if str(equipo['id']) == busqueda:
            if equipo['activo']:
                equipo['activo'] = False
                print(f"\nEl equipo '{equipo['nombre']}' ha sido marcado como INACTIVO.")
                print(f"Estado actual del equipo '{equipo['nombre']}': Inactivo\n")
            else:
                print(f"El equipo '{equipo['nombre']}' ya estaba inactivo.\n")
            return
    
    print("No se encontró un equipo con ese ID.\n")


def menu_equipos(equipos):
    opcion = 0
    while opcion != "6":
        print("""
        1. Crear equipo
        2. Listar equipos
        3. Buscar equipos por ID
        4. Actualizar datos
        5. Eliminar equipos
        6. Salir
        """)
        opcion = input("Dime qué opción quieres realizar: ")

        match opcion:
            case "1": 
                crear_equipo(equipos)
            case "2":
                listar_equipos(equipos)
            case "3":
                buscar_equipo(equipos)
            case "4":
                actualizar_datos(equipos)
            case "5":
                eliminar_equipo(equipos)
            case "6":
                  ("Saliendo al menu principal...")
            case _:
                print("Opción no válida, intenta nuevamente.")

            





