lista_compra = []

producto = (input("Escriba el producto que quiere almacenar en la lista de la compra: "))

while producto != "fin":
	if producto not in lista_compra:
		lista_compra.append(producto)
		print(f"{producto}, ha sido añadido a la lista correctamente")
	
	else:
		print(f"Ya tienes {producto} en la lista de la compra")

	producto = input("Escriba otro producto (o 'fin' para terminar):")


print ("Lista de la compra realizada:")
for item in lista_compra:
	print(f"-{item}")


