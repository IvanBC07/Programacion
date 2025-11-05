frases = ["hola que tal", "buenos dias", "adios hasta mañana"]

def mayuscula(f):
    return f.title()

mayusculas = list(map(mayuscula, frases))

print(mayusculas)