#definimos variables

#definimos las funciones
def num_primo(numero):
    if numero < 2:
        return False
    for i in range (2, numero):
        if numero % i == 0:
            return False
    return True


#definimos el código

print (num_primo(3)) 
print (num_primo(10))
