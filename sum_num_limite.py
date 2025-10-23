#definimos las variables

#Definimos las funciones
def suma_hasta_limite(num_limite):
    suma = 0
    for i in range(1, num_limite + 1):
        suma += i
    return suma


#Definimos el código

print (suma_hasta_limite(3))