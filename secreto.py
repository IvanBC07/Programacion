import random
secreto = random.randint(1, 100)

print("He pensado un número entre 1 y 100. Intenta adivinarlo.")

# Bucle
while True:
	intento = int(input("Ingresa tu número: "))

	if intento < secreto:
		print("Demasiado bajo. Intenta otra vez.")
	elif intento > secreto:
		print("Demasiado alto. Intenta otra vez.")
	else:
		print("¡Correcto! El número era", secreto)
		break