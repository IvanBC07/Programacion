libros = [
    ("Futbolisimos", "Novela"),
    ("50 sombras de grey", "Ensayo"),
    ("Los minions", "Poesía"),
    ("Sexo en las vegas", "Romance"),
]

#Creamos la función
def es_activo(l):
    nombre, genero = l
    return genero == "Novela"

#Creamos el filter
novelas = list(filter(es_activo, libros))

#Mostramos la lista
print(novelas)