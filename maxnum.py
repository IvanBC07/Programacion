numeros = []  

while True:
    numero = input("Ingresa un nombre (o escribe 'hecho' para terminar): ")
    
    if numero == "hecho":  
        break
    
    numero.append(numero)  # Agrega el numero a la lista


print("Lista completa de numeros ingresados:")
print(numeros)

# Mostrar los numeros uno por uno
print("Nombres ingresados:")
for numeros in numeros:
    print(numeros)