# =============================
#      VARIABLES GLOBALES
# =============================

equipos = []
jugadores = []
partidos = []
tabla = []

# =============================
#      IMPORTAR MÓDULOS
# =============================


import funciones_basicas
import modulo_jugadores
import modulo_partidos
import modulo_equipos
import modulo_resultados
from funciones_basicas import leer_fecha_hora, generar_id 


# =============================
#      MENÚ PRINCIPAL
# =============================

def menu_principal():
    menu = "0"
    while menu != "5":
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Gestión de equipos.")
        print("2. Gestión de jugadores.")
        print("3. Calendario de partidos.")
        print("4. Resultado y clasificación")
        print("5. Salir")

        menu = input("Dime qué menú quieres ejecutar: ")

        match menu:
            case "1":
                modulo_equipos.menu_equipos(equipos)
            case "2":
                modulo_jugadores.menu_jugadores(jugadores, equipos)
            case "3":
                modulo_partidos.menu_partidos(partidos, leer_fecha_hora, generar_id, equipos)
            case "4":
                modulo_resultados.menu_resultados(equipos, partidos)
            case "5":
                print("Saliendo del programa....")
            case _ :
                print("No has seleccionado una opción valida.")


# =============================
#      EJECUCIÓN PRINCIPAL
# =============================

menu_principal()