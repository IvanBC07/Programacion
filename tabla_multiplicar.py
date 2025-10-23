numero = int(input("Ingrese un número entero y positivo: "))

if numero <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    for multiplicar in range(1, 11):
        resultado = numero * multiplicar
        print(f"{numero} x {multiplicar} = {resultado}")