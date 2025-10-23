# ---------------------------------------------
# GESTOR DE VIAJES TURÍSTICOS - Ejercicio tipo B
# ---------------------------------------------

# Estructuras principales
viajes = {}          # destino -> (precio, dias)
reservas = []        # lista de destinos reservados (en orden)

# Función auxiliar para leer números válidos
def leer_float(mensaje, minimo):
    valor = 0
    while True:
        try:
            valor = float(input(mensaje))
            if valor > minimo:
                return valor
            else:
                print(f"Debe ser mayor que {minimo}.")
        except ValueError:
            print("Entrada no válida. Usa números.")

def leer_int(mensaje, minimo):
    valor = 0
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= minimo:
                return valor
            else:
                print(f"Debe ser al menos {minimo}.")
        except ValueError:
            print("Entrada no válida. Usa números enteros.")

# Menú principal
opcion = 0
while opcion != 6:
    print("\n--- GESTOR DE VIAJES TURÍSTICOS ---")
    print("1. Añadir viaje al catálogo")
    print("2. Mostrar catálogo")
    print("3. Reservar un destino")
    print("4. Ver reservas")
    print("5. Resumen de coste y días")
    print("6. Salir")
    
    try:
        opcion = int(input("Elige una opción (1-6): "))
    except ValueError:
        print("Opción no válida.")
        continue

    # match case para opciones
    match opcion:
        # 1. Añadir viaje
        case 1:
            destino = input("Destino: ").strip().title()
            if destino in viajes:
                print("El destino ya existe en el catálogo.")
                actualizar = input("¿Deseas actualizarlo? (s/n): ").lower()
                if actualizar != "s":
                    print("Actualización cancelada.")
                else:
                    precio = leer_float("Nuevo precio (>0): ", 0)
                    dias = leer_int("Nuevos días (≥1): ", 1)
                    viajes[destino] = (precio, dias)
                    print(f"{destino} actualizado correctamente.")
            else:
                precio = leer_float("Precio (>0): ", 0)
                dias = leer_int("Días (≥1): ", 1)
                viajes[destino] = (precio, dias)
                print(f"Viaje a {destino} añadido al catálogo.")

        # 2. Mostrar catálogo
        case 2:
            if viajes:
                print("\n--- CATÁLOGO DE VIAJES ---")
                for dest, datos in viajes.items():
                    print(f"{dest} -> {datos[0]:.2f}€ ({datos[1]} días)")
            else:
                print("Catálogo vacío.")

        # 3. Reservar destino
        case 3:
            destino = input("Destino a reservar: ").strip().title()
            if destino in viajes:
                reservas.append(destino)  # Se permiten reservas repetidas
                print(f"Reserva añadida: {destino}")
            else:
                print("Ese destino no existe en el catálogo.")

        # 4. Ver reservas
        case 4:
            if reservas:
                print("\n--- LISTA DE RESERVAS ---")
                for i, dest in enumerate(reservas, start=1):
                    print(f"{i}. {dest}")
            else:
                print("No hay reservas registradas.")

        # 5. Resumen de coste y días
        case 5:
            if reservas:
                total_precio = 0
                total_dias = 0
                for dest in reservas:
                    precio, dias = viajes[dest]
                    total_precio += precio
                    total_dias += dias
                print("\n--- RESUMEN ---")
                print(f"Total a pagar: {total_precio:.2f}€")
                print(f"Total de días: {total_dias}")
                print(f"Número de reservas: {len(reservas)}")
            else:
                print("No hay reservas para resumir.")

        # 6. Salir
        case 6:
            print("Gracias por usar el gestor. ¡Hasta pronto!")

        # Opción no válida
        case _:
            print("Opción no válida. Elige entre 1 y 6.")