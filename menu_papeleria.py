#Creamos el diccionario, la lista y la variable 'opcion'.
productos = {"bolígrafo": 1.2, "cuaderno": 3.5, "carpeta": 2.8}
carrito = []
opcion = 0

while opcion != "5":
    #Creamos el menu que va a ver el usuario
    print ("\n1. Mostrar productos")
    print ("2. Añadir productos a la lista")
    print ("3. Mostrar el carrito")
    print ("4. Ver total de compra")
    print ("5. Salir")
    #Preguntamos por la opción que quiere realizar el usuario.
    opcion = (input("Dime la opcion que quieras hacer (1-4) y presiona ENTER:"))

    match opcion:

        # Creamos cada Case para cada caso
        case "1":
            print("\nProductos disponibles:")
            for producto, precio in productos.items():
                print(f"- {producto}: {precio}€")
        #Preugntamos al usuario los productos que quiere meter en el carrito
        case "2":
            compras = ""
            while compras != "fin":
                compras = (input("Dime que productos quieres agregar a la lista, cuando hayas acabado escribe 'fin': "))
                if compras not in productos:
                     print ("Este producto no esta en el catalogo, revise su escritura...")
                else:
                    carrito.append(compras)
                    print(f"{compras} Ha sido añadido al carrito")
            print (f"Has comprado los siguintes producto: - - -  {carrito} - - -  ")

        #Mostramos el respectivo carrito
        case "3":
            
            print(" - - - - - Aqui tienes tu carrito - - - - - ")
            for item in carrito:
                print(f"- {item}")
            print(" - - - - - - - - - - - - - - - - - - - - - - ")

        #Cremos la variable total para mostrar el total del precio haciendo un bucle for para recorrer cada producto del carrito
        case "4":
                print("Tu carrito contiene:")
                total = 0
                for producto in carrito:
                    precio = productos[producto]
                    print(f"- {producto}: {precio}€")
                    total += precio
                print(f"Total: {total}€")
        
        case "5":
            print ("Muchas gracias por comprar, esperamos que vuelva de nuevo...")
           


