precio = ""

edad = int(input("Dime la edad que tienes :" ))

if edad <5 :
	print ("El precio de la entrada es Gratis")

elif  5 <= edad <= 12:
	print ("El precio de la entrada es de 5 €")

elif  12 <= edad <= 18:
	print ("El precio de la entrada es de 7 €")

else :
	print ("El precio de la entrada es de 10 €")