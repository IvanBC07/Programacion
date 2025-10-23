suma_positivos = 0
contador_positivos = 0

numero = int(input("Introduce un número entero (0 para terminar): "))

while numero != 0:
    
    numero = int(input("Introduce un número entero (0 para terminar): "))

    if numero > 0:
        suma_positivos += numero
        contador_positivos += 1

   

print(f"La suma total de los números positivos es: {suma_positivos}")
print(f"Se han introducido {contador_positivos} números positivos.")