#Definimos las funciones.
def num_max(numero_max):
    maximo = numero_max[3]
    for n in numero_max:
        if n > maximo:
            maximo = n
    return maximo
    

#Definimos el código

print(num_max([2,100,909,10]))
