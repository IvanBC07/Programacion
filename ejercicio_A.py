alumnos = {}
orden_registro = []

def leer_nota(msg):
    nota = -1
    while nota < 0 or nota > 10:
        try:
            nota = float(input(msg))
            if nota < 0 or nota > 10:
                print("Debe estar entre 0 y 10.")
        except:
            print("Número no válido.")
    return nota

op = 0
while op != 5:
    print("\n1. Añadir alumno")
    print("2. Listar alumnos")
    print("3. Media de un alumno")
    print("4. Estadísticas del grupo")
    print("5. Salir")
    try:
        op = int(input("Opción: "))
    except:
        op = 0

    match op:
        case 1:
            nombre = input("Nombre: ").strip().title()
            if nombre in alumnos:
                r = input("Ya existe. ¿Reemplazar notas? (s/n): ").lower()
                if r != "s":
                    print("Cancelado.")
                else:
                    n1 = leer_nota("Nota 1: ")
                    n2 = leer_nota("Nota 2: ")
                    n3 = leer_nota("Nota 3: ")
                    alumnos[nombre] = (n1, n2, n3)
                    print("Notas actualizadas.")
            else:
                n1 = leer_nota("Nota 1: ")
                n2 = leer_nota("Nota 2: ")
                n3 = leer_nota("Nota 3: ")
                alumnos[nombre] = (n1, n2, n3)
                orden_registro.append(nombre)
                print("Alumno añadido.")

        case 2:
            if alumnos:
                for n in orden_registro:
                    if n in alumnos:
                        print(n, "->", alumnos[n])
            else:
                print("No hay alumnos.")

        case 3:
            nombre = input("Nombre: ").strip().title()
            if nombre in alumnos:
                n1, n2, n3 = alumnos[nombre]
                m = (n1 + n2 + n3) / 3
                e = "Aprobado" if m >= 5 else "Suspenso"
                print(f"Media: {m:.2f} -> {e}")
            else:
                print("No existe.")

        case 4:
            if alumnos:
                total = 0
                notas = 0
                aprob = 0
                for ns in alumnos.values():
                    media = sum(ns) / 3
                    total += sum(ns)
                    notas += 3
                    if media >= 5:
                        aprob += 1
                print("Alumnos:", len(alumnos))
                print("Media global:", total / notas)
                print("Aprobados:", (aprob / len(alumnos)) * 100, "%")
            else:
                print("Sin datos.")

        case 5:
            print("Fin del programa.")

        case _:
            print("Opción no válida.")