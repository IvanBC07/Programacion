nombres = []  

while True:
    nombre = input("Ingresa un nombre (o escribe 'fin' para terminar): ")
    
    if nombre == "fin":  
        break
    
    nombres.append(nombre)  # Agrega el nombre a la lista


print("Lista completa de nombres ingresados:")
print(nombres)

# Mostrar los nombres uno por uno
print("Nombres ingresados:")
for nombres in nombres:
    print(nombres)