from funciones_basicas import generar_id, leer_texto, leer_int, imprimir_tabla


def crear_jugador(jugadores, equipos):
    nombre = leer_texto("Nombre del jugador: ")
    posicion = leer_texto("Posición: ")
    equipo_id = leer_int("ID del equipo: ")
    equipo = next((e for e in equipos if e["id"] == equipo_id and e["activo"]), None)
    if not equipo:
        print("Equipo no válido o inactivo.")
        return
    nuevo = {"id": generar_id(jugadores), "nombre": nombre, "posicion": posicion,
             "equipo_id": equipo_id, "activo": True}
    jugadores.append(nuevo)
    print("Jugador agregado.")


def listar_jugadores(jugadores, equipos):
    filas = []
    for j in jugadores:
        if j["activo"]:
            eq = next((e["nombre"] for e in equipos if e["id"] == j["equipo_id"]), "Sin equipo")
            filas.append([j["id"], j["nombre"], j["posicion"], eq])
    imprimir_tabla(filas, ["ID", "Nombre", "Posición", "Equipo"], "Jugadores activos")

def buscar_jugador(jugadores, equipos):
    #Preguntamos por el id del producto que quiere buscar
    busqueda = int(input("Dime el id del jugador que quieres buscar:"))
    for j in jugadores:
        for q in equipos:
        #Si ese id existe en la tabla jugadores en algun jugador, se mostrara los datos:
            if j["id"] == busqueda:
                print("\nJugador encontrado:")
                print("ID:", j["id"])
                print("Nombre:", j["nombre"])
                print("posicion:", j["posicion"])
                print("Equipo", q["nombre"])
                print("Estado:", "Activo" if j["activo"] else "Inactivo")
                print("------------------------")
                return
    #En caso de que no encuentre ese ID mostrar el siguiente mensaje:
    print("No se encontró ningun usuario con ese ID.")

def actualizar_jugadores(jugadores, equipos):
    #Preguntamos por el id del usuario que quiere actualizar:
    actualizar = int(input("Dime el id del jugador que quieres actualizar:"))
    for j in jugadores:
        if j["id"] == actualizar:
            #Preguntamos por los nuevos datos
            nuevo_nombre = input("Nuevo nombre (Deja en blanco para no cambiar): ")
            #Ahora creamos la condicion para que esos nombres cambien el antiguo dato por el nuevo
            if nuevo_nombre != "":
                j['nombre'] = nuevo_nombre

            nueva_posicion = input("Nueva posición (Deja en blanco para no cambiar): ")
            #Ahora creamos la condicion para que esos nombres cambien el antiguo dato por el nuevo
            if nueva_posicion != "":
                j['posicion'] = nueva_posicion

            nuevo_equipo_id = (input("Nuevo id de equipo  (Deja en blanco para no cambiar): "))
            if nuevo_equipo_id != "":
                nuevo_equipo_id = int(nuevo_equipo_id)
                equipo_encontrado = next((e for e in equipos if e['id'] == nuevo_equipo_id and e['activo']), None)
                if equipo_encontrado:
                    j['equipo_id'] = nuevo_equipo_id
                    
                



            #Al acabar mostraremos un mensaje de que se ha modificado correctamente.
            print("jugador actualizado correctamente.\n")
            return

    print("No se encontró un jugador con ese ID.\n")

def eliminar_jugador(jugadores):
    busqueda = int(input("Dime el id del jugador que quieres eliminar (convertir estado a inactivo): "))

    for j in jugadores:
        if j['id'] == busqueda:
            if j['activo']:
                j['activo'] = False
                print(f"\nEl ejugador '{j['nombre']}' ha sido marcado como INACTIVO.")
            else:
                print(f"El jugador '{j['nombre']}' ya estaba inactivo.\n")
            return
    
    print("No se encontró un jugador con ese ID.\n")

def menu_jugadores(jugadores, equipos):
    menu = "0"
    while menu != "6":
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Dar de alta a jugador.")
        print("2. Listar jugadores.")
        print("3. Buscar jugador por ID.")
        print("4. Actualizar jugador")
        print("5. Eliminar jugador")
        print("6.Salir")

        menu = input("\nDime qué menú quieres ejecutar: ")

        match menu:
            case "1":
                crear_jugador(jugadores, equipos)
            case "2":
                listar_jugadores(jugadores, equipos)
            case "3":
                buscar_jugador(jugadores, equipos)
            case "4":
                actualizar_jugadores(jugadores, equipos)
            case "5":
                eliminar_jugador(jugadores)
            case "6":
                ("Saliendo del programa....")
            case _:
                print("No has seleccionado una opción valida.")