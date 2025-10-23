suma = 0
contador = 0

while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break

    suma += numero
    contador += 1

if contador > 0:
    promedio = suma / contador
    print("El promedio de los numeros es:", promedio)
else:
    print("No ingresaste ningun numero")