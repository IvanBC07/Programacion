empleados = [
    ("Maria", "Activo"),
    ("Jorge", "Inactivo"),
    ("Manuel", "Activo"),
    ("Lorena", "Inactivo"),
]

def es_activo(e):
    nombre, estado = e
    return estado == "Activo"

#Creamos el filter
empl_activos = list(filter(es_activo, empleados))

#Mostramos la lista
print(empl_activos)