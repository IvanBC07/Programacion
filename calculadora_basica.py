# Solicitar números al usuario
num1 = float(input("Ingrese el primer número: ")) 
num2 = float(input("Ingrese el segundo número: "))

# Solicitar operación
operacion = input("Ingrese la operación (suma, resta, multiplicacion, division): ")

# Ejecutar operación según la elección
if operacion == "suma":
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)

elif operacion == "resta":
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)

elif operacion == "multiplicacion":
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)

elif operacion == "division":
    if num2 == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)

else:
    print("Operación no válida.")