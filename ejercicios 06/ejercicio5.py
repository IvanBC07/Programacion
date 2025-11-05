Tareas = [
    ("Comer", "Urgente"),
    ("Llevar un paquete", "No urgente"),
    ("Leer", "Urgente"),
]

#Creamos la función
def es_urgente(t):
    nombre, urgencia = t
    return urgencia == "Urgente"

#Creamos el filter
tareas_urgentes = list(filter(es_urgente, Tareas))

#Mostramos la lista
print(tareas_urgentes)