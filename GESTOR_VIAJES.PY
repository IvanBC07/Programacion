
destinos = ("Italia", "Barcelona", "Colombia","Paris")
opcion = 0
precio = 0
dias = 0
catalogo = {
    "Italia": (300, 55),
    "Barcelona": (1290, 4),
    "Colombia": (199, 2),
    "Paris": (2300, 7)
}

while opcion != "6":
    print("--- TU MEJOR VIAJE ---")
    print("opcion 1: Añadir viaje al catalogo")
    print("opcion 2: Mostrar catalogo")
    print("opcion 3: Reservar un destino")
    print("opcion 4: Ver reservas")
    print("opcion 5: Resumen de coste y dias")
    print("opcion 6: salir")
    opcion = (input("Pon el numero para decirme que quieres hacer:"))
    
    
    if opcion == "1":
        
            print (destinos)
            destino = (input("Dime que destinos quieres visitar:"))
            if destino not in destinos:
                 print ("Destino no permitido")
            dias = (input("Cuantos dias contendrá el viaje:"))
            precio = input("Dime que precio quieres poner al viaje por dia:")
            catalogo[destino] = (precio, dias)
    elif opcion == "2":
    
                print(catalogo)


    elif opcion == "6":
           print ("Muchas gracias por reservar con nosotros")
           

    elif opcion == "5":
          print (f"- Iras a {destino}")
          print (f"- Precio a pagar {precio}€ por dia ")
          print (f"- Una cantidad de {dias} dias")





          
          

          
          
          



            
            
