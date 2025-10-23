saldo = 100
opcion = ""
print(f"Bienvenido al cajero, tienes un saldo de {saldo}€")

while opcion != "4":
    print("\n--- CAJERO AUTOMÁTICO ---")
    print("opcion 1: Agregar dinero")
    print("opcion 2: Retirar dinero")
    print("opcion 3: Consultar saldo")
    print("opcion 4: Salir")
   
    opcion = input("Que opcion quieres realizar: ")

    if opcion == "3":
        print(f"Tienes un saldo de {saldo} €")

    elif opcion == "2":
        retirar = int(input("Cuanto dinero quieres retirar: "))
        if retirar > saldo:
            print(f"No tienes suficiente saldo para retirar {retirar}€, solo tienes {saldo}€")
        else:
            saldo -= retirar
            print(f"Has retirado {retirar}€, tu saldo actual es {saldo}€")

    elif opcion == "1":
        agregar = int(input("Cuanto dinero quieres agregar: "))
        saldo += agregar
        print(f"Has agregado {agregar}€, tu saldo actual es {saldo}€")

    elif opcion == "4":
        print(f"Tienes un saldo de {saldo}€, saliendo del cajero...")

    else:
        print("Opción no válida, por favor intenta de nuevo.")
	
		