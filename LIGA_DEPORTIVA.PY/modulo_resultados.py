from funciones_basicas import leer_int, imprimir_tabla

def registrar_resultado(partidos, equipos):
    if not partidos:
        print("No hay ningún partido registrado.")
        return

    # Filtrar partidos pendientes
    pendientes = [p for p in partidos if not p.get('jugado', False)]

    if not pendientes:
        print("Todos los partidos ya tienen su resultado.")
        return

    print("\n--- Partidos pendientes ---")
    for p in pendientes:
        # Aseguramos que los IDs sean enteros para la comparación
        local = next((e["nombre"] for e in equipos if int(e["id"]) == int(p["local_id"])), 'Desconocido')
        visitante = next((e["nombre"] for e in equipos if int(e["id"]) == int(p["visitante_id"])), 'Desconocido')
        print(f"ID {p['id']}: Jornada {p['jornada']}  {local} vs {visitante} ({p['fecha']} {p['hora']})")

    # Pedir ID del partido a registrar
    id_partido = int(input("\nDime el id del partido que quieres registrar el resultado: "))
    partido = next((p for p in partidos if int(p['id']) == id_partido), None)

    if partido is None:
        print("No se encontró el partido.")
        return

    if partido.get('jugado', False):
        print("Este partido ya tiene resultado.")
        return

    # Pedir goles
    goles_local = int(input("Dime los goles del equipo local: "))
    goles_visitante = int(input("Dime los goles del equipo visitante: "))

    # Guardar resultado
    partido['resultado'] = (goles_local, goles_visitante)
    partido['jugado'] = True

    print("Resultado registrado correctamente.")


def calcular_clasificacion(equipos, partidos):
    tabla = []
    for e in equipos:
        pj = g = e_ = p_ = gf = gc = 0  # 

        # Recorremos cada partido
        for m in partidos:
            if m["jugado"]:  # Solo procesamos partidos jugados
                gL, gV = m["resultado"]  # goles local y visitante

                if e["id"] == m["local_id"]:  # Equipo local
                    pj += 1
                    gf += gL
                    gc += gV

                    if gL > gV:
                        g += 1
                    elif gL == gV:
                        e_ += 1
                    else:
                        p_ += 1

                elif e["id"] == m["visitante_id"]:  # Equipo visitante
                    pj += 1
                    gf += gV
                    gc += gL

                    if gV > gL:
                        g += 1
                    elif gV == gL:
                        e_ += 1
                    else:
                        p_ += 1

        pts = g * 3 + e_ * 1  # Puntos totales
        dg = gf - gc           

        tabla.append({
            "Equipo": e["nombre"],
            "PJ": pj,
            "G": g,
            "E": e_,
            "P": p_,
            "GF": gf,
            "GC": gc,
            "DG": dg,
            "PTS": pts
        })

    # Ordenamos la tabla, esto he tenido que preguntarle a chatGPT
    tabla.sort(key=lambda x: (-x["PTS"], -x["DG"], -x["GF"], x["Equipo"]))

    # Mostrar tabla usando la función auxiliar imprimir_tabla
    if tabla:
        filas = [[t["Equipo"], t["PJ"], t["G"], t["E"], t["P"], t["GF"], t["GC"], t["DG"], t["PTS"]] for t in tabla]
        columnas = ["Equipo", "PJ", "G", "E", "P", "GF", "GC", "DG", "PTS"]
        imprimir_tabla(filas, columnas)
    else:
        print("No hay equipos para mostrar.")

    return tabla

def estaditicas_equipo (partidos, equipos):
    id_equipo = int(input("Dime el id del equipo del que quieres ver las estadísticas: "))

    # Buscar el equipo
    equipo = next((e for e in equipos if int(e["id"]) == id_equipo), None)
    if equipo is None:
        print("No se encontró el equipo.")
        return

    # Inicializar estadísticas
    pj = g = e_ = p_ = gf = gc = 0

    # Recorrer los partidos
    for m in partidos:
        if not m.get('jugado', False):
            continue  # ignorar partidos no jugados

        gL, gV = m["resultado"]

        if id_equipo == int(m["local_id"]):
            pj += 1
            gf += gL
            gc += gV
            if gL > gV:
                g += 1
            elif gL == gV:
                e_ += 1
            else:
                p_ += 1

        elif id_equipo == int(m["visitante_id"]):
            pj += 1
            gf += gV
            gc += gL
            if gV > gL:
                g += 1
            elif gV == gL:
                e_ += 1
            else:
                p_ += 1

    pts = g * 3 + e_
    dg = gf - gc

    resumen = {
        "Equipo": equipo["nombre"],
        "PJ": pj,
        "G": g,
        "E": e_,
        "P": p_,
        "GF": gf,
        "GC": gc,
        "DG": dg,
        "PTS": pts
    }

    print("\n--- Estadísticas del equipo ---")
    for k, v in resumen.items():
        print(f"{k}: {v}")

    return resumen



def menu_resultados(equipos, partidos):
    opcion = 0
    while opcion != "4":
        print("""
        1. Registrar resultado
        2. Mostrar clasificación
        3. Estadisticas equipo
        4. Salir al menu principal
        """)
        opcion = input("Dime qué opción quieres realizar: ")

        match opcion:
            case "1": 
                registrar_resultado(partidos, equipos)
            case "2":
                calcular_clasificacion(equipos, partidos)
            case "3":
                estaditicas_equipo(partidos, equipos)
            case "4":
                ("Saliendo el menu principal...")
            case _:
                print("Opción invalida")

            

