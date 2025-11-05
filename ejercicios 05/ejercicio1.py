numeros = [1,2,3,4,5,6,7]

def sumar_5(n):
    return n + 5

sumados = list(map(sumar_5, numeros))

print(sumados)