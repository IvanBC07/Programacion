# Definimos las variables y la lista de los articulos
articulos = [] 
opcion = 0
usuarios = []
usuario_activo = None
ventas = []
carrito_actual = []

#Definimos las funciones

#La primera servira para generar un id cada vez que creemos un nuevo producto
def generar_id(lista):
    """Devuelve un ID nuevo basado en los existentes."""
    if not lista:  # si la lista está vacía
        return 1
    else:
        # busca el ID más alto y suma 1
        return max(item["id"] for item in lista) + 1
    

def crear_articulo():
    print("\n--- Crear nuevo artículo ---")

    #Indicamos que el id del articulo lo saque de la funcion de "generar_id()"
    id_articulo = generar_id(articulos)
    print(f"ID asignado automáticamente: {id_articulo}")

    #Preguntamos por los datos del producto
    nombre = input("Ingrese el nombre del artículo: ")
    precio = float(input("Ingrese el precio del artículo (formato XX.XX): "))
    stock = int(input("Ingrese el stock disponible: "))

    #Definimos los datos
    nuevo_articulo = {
        "id": id_articulo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "activo": True
    }
    articulos.append(nuevo_articulo)
    print(f"Artículo '{nombre}' agregado correctamente con ID {id_articulo}.\n")

def listar_articulos():
    print("\n--- Lista de artículos ---")
    #Preguntamos al usuario si quiere que mostremos los productos activos o inactivos
    estado = (input("Mostrar productos: 1. Activos   2. Inactivos:"))
    for art in articulos:
        # Determinar lo que se muestra según la opción
         if estado == "1" and art["activo"] == True:
            print("ID:", art["id"])
            print("Nombre:", art["nombre"])
            print("Precio:", art["precio"])
            print("Stock:", art["stock"])
            print("Estado: Activo")
            print("------------------------")
        
        # Mostrar solo inactivos
         elif estado == "2" and art["activo"] == False:
            print("ID:", art["id"])
            print("Nombre:", art["nombre"])
            print("Precio:", art["precio"])
            print("Stock:", art["stock"])
            print("Estado: Inactivo")
            print("------------------------")


def buscar_producto():
    #Preguntamos por el id del producto que quiere buscar
    busqueda = int(input("Dime el id del producto que quieres buscar:"))
    for art in articulos:
        #Si ese id existe en la tabla articulos en alguno, se mostrara los datos:
        if art["id"] == busqueda:
            print("Artículo encontrado:")
            print("ID:", art["id"])
            print("Nombre:", art["nombre"])
            print("Precio:", art["precio"])
            print("Stock:", art["stock"])
            print("Estado:", "Activo" if art["activo"] else "Inactivo")
            print("------------------------")
            return
    #En caso de que no encuentre ese ID mostrar el siguiente mensaje:
    print("No se encontró un artículo con ese ID.")


def actualizar_articulo():
    #Preguntamos por el id del producto que quiere actualizar:
    actualizar = int(input("Dime el id del producto que quieres actualizar:"))
    for articulo in articulos:
        if articulo["id"] == actualizar:
            #Preguntamos por los nuevos datos
            nuevo_nombre = input("Nuevo nombre (Deja en blanco para no cambiar): ")
            #Ahora creamos la condicion para que esos nombres cambien el antiguo dato por el nuevo
            if nuevo_nombre != "":
                articulo['nombre'] = nuevo_nombre

            nuevo_precio = input("Nuevo precio (Deja en blanco para no cambiar): ")
            if nuevo_precio != "":
                articulo['precio'] = float(nuevo_precio)

            nuevo_stock = input("Nuevo stock (Deja en blanco para no cambiar): ")
            if nuevo_stock != "":
                articulo['stock'] = int(nuevo_stock)

            #Al acabar mostraremos un mensaje de que se ha modificado correctamente.
            print("Artículo actualizado correctamente.\n")
            return

    print("No se encontró un artículo con ese ID.\n")


def eliminar_articulo():
    #Preguntamos por el id del producto que quiere eliminar
    eliminar = int(input("Dime el id del producto que quieres eliminar:"))
    for articulo in articulos:
        if articulo["id"] == eliminar:
            #Usamos el parametro remove para eliminar el articulo.
            articulos.remove(articulo)
            print("Artículo eliminado correctamente.\n")
            return
    print("No se encontró un artículo con ese ID.")


def alternar_estado():
    #Preguntamos por el id del producto que quiere alternar el estado
    id_cambiar = int(input("Dime el ID del producto a alternar estado: "))
    for art in articulos:
        if art["id"] == id_cambiar:
            art["activo"] = not art["activo"]
            #En este apartado, tenemos que crear una línea en la cual si el estado esta en activo, haga que cambie a inactivo.
            estado = "Activo" if art["activo"] else "Inactivo"
            print(f"Estado cambiado a {estado}.\n")
            return
    print("No se encontró un artículo con ese ID.")


def menu_articulos():
    #Creación del menu.
    opcion = 0
    while opcion != "7":
        print("""
        1. Crear artículo
        2. Listar artículos
        3. Buscar artículo por ID
        4. Actualizar artículo
        5. Eliminar artículo
        6. Alternar activo/inactivo
        7. Salir
        """)
        opcion = input("Dime qué opción quieres realizar: ")

        match opcion:
            case "1": 
                crear_articulo()
            case "2":
                listar_articulos()
            case "3":
                buscar_producto()
            case "4":
                actualizar_articulo()
            case "5":
                eliminar_articulo()
            case "6":
                alternar_estado()
            case "7":
                print("Saliendo del programa...")
            case _:
                print("Opción no válida, intenta nuevamente.")



# ++++++++++++ USUARIOS ++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++
# ++++++++++++ USUARIOS ++++++++++++++++
 

def crear_usuario():
    print("\n--- Crear nuevo usuario ---")

    # ID automático
    id_usuario = generar_id(usuarios)
    print(f"ID asignado automáticamente: {id_usuario}")

    # Nombre
    nombre = input("Ingrese el nombre del usuario: ")

    # Validación básica del email sin while True ni break
    email_valido = False
    email = ""
    while not email_valido:
        email = input(f"Ingrese el email de {nombre}: ")
        if "@" in email and "." in email:
            email_valido = True
        else:
            print("Email inválido. Debe contener '@' y '.'")

    # Definimos los datos
    usuario = {
        "id": id_usuario,
        "nombre": nombre,
        "email": email,
        "activo": True
    }

    # Agregamos a la lista correcta
    usuarios.append(usuario)
    print ("Usuario creado correctamente")

def listar_usuarios():
    print("\n--- Lista de usuarios ---")
    #Preguntamos al usuario si quiere que mostremos los usuarios activos o inactivos
    estado = (input("Mostrar usuarios: 1. Activos   2. Inactivos:"))
    for user in usuarios:
        # Determinar lo que se muestra según la opción
         if estado == "1" and user["activo"] == True:
            print("ID:", user["id"])
            print("Nombre:", user["nombre"])
            print("email:", user["email"])
            print("Estado: Activo")
            print("------------------------")
        
        # Mostrar solo inactivos
         elif estado == "2" and user["activo"] == False:
            print("ID:", user["id"])
            print("Nombre:", user["nombre"])
            print("email:", user["email"])
            print("Estado: Activo")
            print("------------------------")


def buscar_usuarios():
    #Preguntamos por el id del usuario que quiere buscar
    busqueda = int(input("Dime el id del usuario que quieres buscar:"))
    for user in usuarios:
        #Si ese id existe en la tabla usuarios en algun user, se mostrara los datos:
        if user["id"] == busqueda:
            print("Artículo encontrado:")
            print("ID:", user["id"])
            print("Nombre:", user["nombre"])
            print("email:", user["email"])
            print("Estado:", "Activo" if user["activo"] else "Inactivo")
            print("------------------------")
            return
    #En caso de que no encuentre ese ID mostrar el siguiente mensaje:
    print("No se encontró ningun usuario con ese ID.")


def actualizar_usuarios():
    #Preguntamos por el id del usuario que quiere actualizar:
    actualizar = int(input("Dime el id del usuario que quieres actualizar:"))
    for user in usuarios:
        if user["id"] == actualizar:
            #Preguntamos por los nuevos datos
            nuevo_nombre = input("Nuevo nombre (Deja en blanco para no cambiar): ")
            #Ahora creamos la condicion para que esos nombres cambien el antiguo dato por el nuevo
            if nuevo_nombre != "":
                user['nombre'] = nuevo_nombre

            nuevo_email = input("Nuevo email (Deja en blanco para no cambiar): ")
            if nuevo_email != "":
                user['precio'] = (nuevo_email)

            #Al acabar mostraremos un mensaje de que se ha modificado correctamente.
            print("Usuario actualizado correctamente.\n")
            return

    print("No se encontró un artículo con ese ID.\n")


def eliminar_usuarios():
    #Preguntamos por el id del usuario que quiere eliminar
    eliminar = int(input("Dime el id del usuario que quieres eliminar:"))
    for user in usuarios:
        if user["id"] == eliminar:
            #Usamos el parametro remove para eliminar el usuario-
            usuarios.remove(user)
            print("Usuario eliminado correctamente.\n")
            return
    print("No se encontró un usuario con ese ID.")


def alternar_estado_usuarios():
    #Preguntamos por el id del producto que quiere alternar el estado
    id_cambiar = int(input("Dime el ID del producto a alternar estado: "))
    for user in usuarios:
        if user["id"] == id_cambiar:
            user["activo"] = not user["activo"]
            #En este apartado, tenemos que crear una línea en la cual si el estado esta en activo, haga que cambie a inactivo.
            estado = "Activo" if user["activo"] else "Inactivo"
            print(f"Estado cambiado a {estado}.\n")
            return
    print("No se encontró un artículo con ese ID.")


def menu_usuarios():
    #Creación del menu.
    opcion = 0
    while opcion != "7":
        print("""
        1. Crear usuario
        2. Listar usuarios
        3. Buscar usuario por ID
        4. Actualizar usuario
        5. Eliminar usuario
        6. Alternar activo/inactivo
        7. Salir
        """)

        opcion = input("Dime qué opción quieres realizar: ")

        match opcion:
            case "1": 
                crear_usuario()
            case "2":
                listar_usuarios()
            case "3":
                buscar_usuarios()
            case "4":
                actualizar_usuarios()
            case "5":
                eliminar_usuarios()
            case "6":
                alternar_estado_usuarios()
            case "7":
                print("Saliendo del programa...")
            case _:
                print("Opción no válida, intenta nuevamente.")




# ++++++++++++ CARRITO +++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++
# ++++++++++++ CARRITO +++++++++++++++++


# Seleccionar usuario activo
def seleccionar_usuario(usuarios):
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    print("Usuarios activos:")
    for u in usuarios:
        if u["activo"]:
            print(u["id"], u["nombre"])
    uid = int(input("Ingrese ID del usuario: "))
    # Actualizamos usuario_activo modificando el valor directamente
    for u in usuarios:
        if u["id"] == uid and u["activo"]:
            # Asignamos directamente a la variable global definida al inicio
            globals()['usuario_activo'] = uid
            print(f"Usuario activo: {u['nombre']}")
            return
    print("Usuario no válido o inactivo.")


# Añadir artículo al carrito
def añadir_carrito(carrito, articulos):
    if usuario_activo is None:
        print("Seleccione un usuario activo primero.")
        return
    print("Artículos disponibles:")
    for a in articulos:
        if a["activo"]:
            print(f"{a['id']} {a['nombre']} - Stock: {a['stock']} - €{a['precio']}")
    aid = int(input("Ingrese ID del artículo: "))
    cantidad = int(input("Cantidad: "))
    for a in articulos:
        if a["id"] == aid and a["activo"]:
            if cantidad > a["stock"]:
                print("No hay suficiente stock.")
                return
            # Si el artículo ya está en el carrito, sumamos cantidad
            for item in carrito:
                if item["id"] == aid:
                    item["cantidad"] += cantidad
                    print("Cantidad actualizada en carrito.")
                    return
            # Si no estaba en el carrito, lo agregamos
            carrito.append({"id": aid, "cantidad": cantidad})
            print("Artículo añadido al carrito.")
            return
    print("Artículo no encontrado.")


# Quitar artículo del carrito
def quitar_carrito(carrito):
    if not carrito:
        print("Carrito vacío.")
        return
    aid = int(input("Ingrese ID del artículo a quitar: "))
    for item in carrito:
        if item["id"] == aid:
            carrito.remove(item)
            print("Artículo eliminado del carrito.")
            return
    print("Artículo no encontrado en el carrito.")


# Ver carrito
def ver_carrito(carrito, articulos):
    if not carrito:
        print("Carrito vacío.")
        return
    total = 0
    print("--- Carrito ---")
    for item in carrito:
        for a in articulos:
            if a["id"] == item["id"]:
                subtotal = a["precio"] * item["cantidad"]
                print(f"{a['nombre']} x{item['cantidad']} - €{subtotal}")
                total += subtotal
    print("Total:", total)


# Confirmar compra
def confirmar_compra():
    if usuario_activo is None or not carrito_actual:
        print("No hay usuario activo o el carrito está vacío.")
        return

    total = 0
    venta_items = []

    for item in carrito_actual:
        for a in articulos:
            if a["id"] == item["id"] and a["activo"]:
                if item["cantidad"] > a["stock"]:
                    print(f"No hay suficiente stock de {a['nombre']}.")
                    return
                subtotal = a["precio"] * item["cantidad"]
                total += subtotal
                a["stock"] -= item["cantidad"]
                venta_items.append({
                    "id": a["id"],
                    "cantidad": item["cantidad"],
                    "precio": a["precio"]
                })

    # Crear venta y añadir a la lista global sin reasignar
    ventas.append({
        "id_venta": generar_id(ventas),
        "usuario_id": usuario_activo,
        "items": venta_items,
        "total": total
    })

    # Vaciar el carrito sin reasignar la variable
    carrito_actual.clear()
    print(f"Compra confirmada. Total: €{total}")


# Vaciar carrito
def vaciar_carrito(carrito):
    carrito.clear()
    print("Carrito vaciado.")


# Historial de ventas por usuario
def historial_ventas(ventas):
    if usuario_activo is None:
        print("Seleccione un usuario activo primero.")
        return
    #Recorre todas las ventas en su respectiva lista y comprueba si el id del usuario es el usuario activo
    usuario_ventas = [v for v in ventas if v["usuario_id"] == usuario_activo]
    if not usuario_ventas:
        print("No hay ventas registradas para este usuario.")
        return
    print(f"--- Historial de ventas del usuario {usuario_activo} ---")
    for v in usuario_ventas:
        print(f"Venta #{v['id_venta']} - Total: €{v['total']}")
        for item in v["items"]:
            print(f"  Artículo {item['id']} x{item['cantidad']} - €{item['precio']}")


# Menú de carrito
def menu_carrito():
    carrito = 0
    while carrito != "8":
        print("\n1. Seleccionar usuario activo")
        print("2. Añadir artículo al carrito")
        print("3. Quitar artículo del carrito")
        print("4. Ver carrito")
        print("5. Confirmar compra")
        print("6. Historial de ventas por usuario")
        print("7. Vaciar carrito")
        print("8. Volver")

        carrito = input("Dime que opción quieres realizar:")
        match carrito:
            case "1":
                seleccionar_usuario(usuarios)
            case "2":
                añadir_carrito(carrito_actual, articulos)
            case "3":
                quitar_carrito(carrito_actual)
            case "4":
                ver_carrito(carrito_actual, articulos)
            case "5":   
                confirmar_compra()
            case "6":
                historial_ventas(ventas)
            case "7":
                vaciar_carrito(carrito_actual)
            case "8":
                print("Saliendo del menu...")
            case _:
                print("Opcion no valida")







def menu_principal():
    menu = 0
    while menu != "4":
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Artículos")
        print("2. Usuarios")
        print("3. Carrito y ventas")
        print("4. Salir")

        menu = (input("Dime que menu quieres ejecutar:"))
        match menu:
            case "1":
                menu_articulos()
            case "2":
                menu_usuarios()
            case "3":
                menu_carrito()
            case "4":
                print ("Saliendo del programa....")
        
    
            
#Ejecutamos el menu principal, que contiene todas las demas funciones 

menu_principal()