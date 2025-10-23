#definimos las variables
list_numeros = [1,3,4,6,8,10,14]

#definimos las funciones 
def contar_pares(numeros):
    contador = 0
    for numero in numeros:
        if numero % 2 == 0:
            contador += 1
    return contador


resultado = contar_pares (list_numeros)
print ("La cantidad de numeros pares:", resultado)