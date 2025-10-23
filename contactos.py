agenda = {}



while nombre != "fin" : 

	nombre = (input("Pon el contacto que quieres agregar a la agenda o 'Fin' cuando quieras acabar:"));
	telefono = input(f"Ingrese el número de teléfono de {nombre}: ");
    	agenda[nombre] = telefono # Guardamos en el diccionario;


print (agenda)


