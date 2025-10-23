Inventario = {}

producto = (input("Dime el nombre del producto que quieras guardar en el inventario o escribe 'fin' para terminar:"))


while producto != "fin":
        cantidad = (input(f"Dime la cantidad del stock de {producto}:"))
        Inventario[producto]= cantidad

        producto = (input("Dime el nombre del producto que quieras guardar en el inventario o escribe 'fin' para terminar:"))

print("Inventario final de la tienda:")
for producto, cantidad in Inventario.items():
    print(f"- {producto}: {cantidad} unidades")