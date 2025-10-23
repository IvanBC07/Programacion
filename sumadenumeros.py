# Solicitar número al usuario
N = int(input("Ingrese un número entero positivo: "))

# Verificar si es positivo
if N > 0:
    suma = 0
    for i in range(1, N + 1):
        suma += i
    print("La suma de los primeros", N, "números es:", suma)
else:
    print("Error: Debe ingresar un número entero positivo.")
