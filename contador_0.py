numero = input("Dame una serie de números y te diré cuántos 0 hay en esa serie: ")
contador = 0

for num0 in numero:
    if num0 == "0":
        contador += 1

print("En esa serie de números hay", contador, "ceros.")