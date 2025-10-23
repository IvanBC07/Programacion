num1 = int(input("Introduce el numero 1ero a ingresar:"))
num2 = int(input("Introduce el numero 2º a ingresar:"))

if num1 < 0 :
	print ("Deme un número mayor que 0");

else :
	operacion =(input("Ahora elige suma o resta o  multiplicacion o cerrar:"))
	
	if operacion == "suma":
		resultado = num1 + num2
		print ("El resultado de la suma es:" ,resultado)

	elif operacion == "resta":
		resultado_resta = num1 - num2
		print ("El resultado de la resta es:" ,resultado_resta)

	elif operacion == "multiplicacion":
		resultado_mult = num1 * num2
		print ("El resultado de la multiplicación es:" ,resultado_mult)
	
	else:
		print ("Has acabado")

	

		