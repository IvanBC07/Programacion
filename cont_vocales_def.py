#Definimos las variables


#Definimos las funciones:
def cont_vocales(texto):
    contador = 0
    vocales = "aeiouAEIOU"
    for letra in texto:
        if letra in vocales: 
            contador += 1
    return contador

#Definimos el código
print(cont_vocales("palabra de Ivan"))      
      