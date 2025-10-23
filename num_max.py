numeros = []
numero = ""  

while numero != "hecho":
    numero = input("Dime un número o escribe 'hecho' para terminar: ")
    if numero != "hecho":
            numero_int = int(numero)  
            numeros.append(numero_int)
    

print("Lista de números ingresados:", numeros)

if numeros: 
    mayor_numero = max(numeros)
    print("El número mayor es:", mayor_numero)
else:
    print("No se ingresaron números.")