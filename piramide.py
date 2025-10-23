# 1. Pedimos la altura al usuario
altura = int(input("Introduce la altura de la pirámide: "))

# 2. Usamos un bucle for para controlar las filas
for piramide in range(1, altura + 1):
    # 3. En cada fila mostramos i asteriscos
    print("*" * piramide)