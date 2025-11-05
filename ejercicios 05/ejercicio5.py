palabras = ["Hola", "Buenas", "Profesor"]

def contar_letras(p):
    return len(p)

contador_letras = list(map(contar_letras, palabras))

print(contador_letras)