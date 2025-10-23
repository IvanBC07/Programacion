numero = int(input("Cual es el número entero: "))
cont_pares = 0
for numeros in range(1, numero + 1):
    if numeros % 2 == 0:  
        cont_pares += 1
print("Cantidad de núm pares desde 1 hasta", numero, "es:", cont_pares)

