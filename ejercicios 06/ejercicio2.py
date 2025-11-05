vehiculos = [
    ("Lamborghini", "Aprobada"),
    ("BMW", "Pendiente"),
    ("Mercedes", "Aprobada")
]

def es_aprobado(vehiculo):
    nombre, estado = vehiculo
    return estado == "Aprobada"

vehiculos_aprobados = list(filter(es_aprobado, vehiculos))

print (vehiculos_aprobados)