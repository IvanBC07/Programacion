aprobados = 0
suspensos = 0

nombre = (input("Dime el nombre de el alumno o 'fin' para terminar:"))

while nombre != "fin":
    nota1 = float(input(f"Dime la primera nota de {nombre}:"))
    nota2 = float(input(f"Dime la segunda nota de {nombre}:"))
    nota3 = float(input(f"Dime la tercera nota de {nombre}:"))

    media = (nota1 + nota2 + nota3) / 3

    print (f"La media de {nombre} es de {media}")

    if media < 5:
        print (f"{nombre} ha suspendido porque no llega al 5")
        aprobados += 1
    elif media >= 5:
         print (f"{nombre} ha aprobado porque llega al 5")
         suspensos += 1
         
    nombre = (input("Dime el nombre de el alumno o 'fin' para terminar:"))


print (f"El numero de aprobados es {aprobados}")
print (f"El numero de suspensos es {suspensos}")