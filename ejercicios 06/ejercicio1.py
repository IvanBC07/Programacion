productos = [
    ("Manzana", "Perecedero"),
    ("Arroz", "No perecedero"),
    ("Lechuga", "Perecedero"),
    ("Lata de atún", "No perecedero"),
    ("Plátano", "Perecedero")
]

def perecedero(p):
    nombre, tipo = p
    return tipo == "Perecedero"

perecederos = list(filter(perecedero, productos))

print(perecederos)

    