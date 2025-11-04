import  funciones_basicas

def crear_partido (equipos, leer_fecha_hora, generar_id, partidos):
    jornada = int(input("Jornada (≥1): "))
    local_id = int(input("ID equipo local: "))
    visitante_id = int(input("ID equipo visitante: "))

    if local_id == visitante_id:
        print("Un equipo no puede jugar contra sí mismo.")
        return
    
    # Buscar equipos
    equipo_local = None
    equipo_visitante = None
    for e in equipos:
        if e['id'] == local_id:
            equipo_local = e
        if e['id'] == visitante_id:
            equipo_visitante = e

    if equipo_local is None or equipo_visitante is None:
        print("Alguno de los equipos no existe.")
        return

    # Validar que estén activos
    if equipo_local['activo'] == False:
        print("El equipo local no está activo.")
        return
    if equipo_visitante['activo'] == False:
        print("El equipo visitante no está activo.")
        return

    fecha, hora = leer_fecha_hora()

    partido = {
        "id": generar_id(partidos),
        "jornada": jornada,
        "local_id": local_id,
        "visitante_id": visitante_id,
        "fecha": fecha,
        "hora": hora,
        "jugado": False,
        "resultado": None
    }

    partidos.append(partido)
    print ("Partido creado correctamente.")
def listar_partidos(equipos, partidos):
    if not partidos:
        print("No hay partidos registrados.")
        return

    filtrar = int(input("Filtrar: 1. Por jornada   2. Mostrar todos : "))

    if filtrar == 1:
        jornada = int(input("¿Qué jornada quieres ver?: "))
        lista = [p for p in partidos if p["jornada"] == jornada]
    else:
        lista = partidos

    if not lista:
        print("No hay partidos para esa jornada.")
        return

    print("\n=== LISTA DE PARTIDOS ===")
    for p in lista:
        # Buscar nombres de los equipos por id
        local = next((e["nombre"] for e in equipos if e["id"] == p["local_id"]), "Desconocido")
        visitante = next((e["nombre"] for e in equipos if e["id"] == p["visitante_id"]), "Desconocido")

        # Mostrar resultado si el partido ya se ha jugado
        if p["jugado"]:
            resultado = f"{p['resultado'][0]} - {p['resultado'][1]}"
        else:
            resultado = "Pendiente"

        print(f" Id: {p['id']}   |   Jornada {p['jornada']} | {local} vs {visitante} | {p['fecha']} {p['hora']} | {resultado}")

def repogramar_partido(partidos, leer_fecha_hora):
    id_partido_cambio = int(input("Dime el id del partido que quieres reprogramar:"))
    encontrado = False
    for p in partidos:
        if p['id'] == id_partido_cambio:
            encontrado = True
            if p['jugado']:
                print ("Ese partido ya ha sido jugado, no se puede reprogramar")
                return
            else:
                print(f"Partido Encontrado: Jornada {p['jornada']}  --- Local {p['local_id']}  VS  Visitante {p['visitante_id']}")
                fecha, hora = leer_fecha_hora()
            
            p['fecha'] = fecha
            p['hora'] = hora

            print ("Partido reprogramado correctamente")
            return
    if not encontrado:
        print ("Partido no encontrado")

def eliminar_partido(partidos):
    id_eliminar = int(input("Dime el id del partido que quieres eliminar:"))
    for p in partidos:
        if p['id'] == id_eliminar:
            if p['jugado']:
                print("No se puede eliminar un partido ya jugado.")
                return
            else:
                partidos.remove(p)
                print ("El partido ha sido eliminado correctamente.")
                return
            
        print ("No se ha encontrado ningún partido con ese Id")


def menu_partidos(partidos, leer_fecha_hora, generar_id, equipos):
    opcion = 0
    while opcion != "5":
        print("""
        1. Crear Partido
        2. Listar Partidos
        3. Reprogramar partido
        4. Eliminar partido
        5. Salir al menu principal
        """)
        opcion = input("Dime qué opción quieres realizar: ")

        match opcion:
            case "1": 
                crear_partido(equipos, leer_fecha_hora, generar_id, partidos)
            case "2":
                listar_partidos(equipos, partidos)
            case "3":
                repogramar_partido(partidos, leer_fecha_hora)
            case "4":
                eliminar_partido(partidos)
            case "5":
                ("Saliendo el menu principal...")
            case _:
                print("Opción invalida")
                
           

            


    

