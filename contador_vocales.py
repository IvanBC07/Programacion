texto = input("Ingrese una cadena de texto: ") 
vocales = "aeiouAEIOU"
contador = 0

for letra in texto:
	if letra in vocales: 
		contador += 1

print("La cantidad de vocales es:", contador)
