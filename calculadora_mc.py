opcion = ""


#Creamos el bucle 

while opcion != "5":

    print("******** CALCULADORA AUTOMÁTICA ********")
    print("opcion 1: Sumar")
    print("opcion 2: Restar")
    print("opcion 3: Multiplicar")
    print("opcion 4: Dividir")
    print("opcion 5: Salir")


#Preguntamos la opcion que quiera elegir, si es 5, se tiene que cortar el bucle.
    opcion = input("Elige una opción (1-5): ")
    if opcion == "5":
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break

#Creamos la variable de los números.
    num1 = float(input("Dime el primer numero con el que quieras operar:"))
    num2 = float(input("Dime el segundo numero con el que quieras operar:"))


   
#Creamos esta condicion para que si el usuario ingresa un numero que no es uno de estos, pedirle que repita.

    if opcion not in ["1", "2", "3", "4"]:
        print("Opción inválida. Intenta de nuevo.")
        continue


#Ahora creamos la matchcase para cada opcion de la calculadora.
    match opcion:
        case "1":
            resultado = num1 + num2
            print(f"{num1} + {num2} = {resultado}")
        case "2":
            resultado = num1 - num2
            print(f"{num1} - {num2} = {resultado}")
        case "3":
            resultado = num1 * num2
            print(f"{num1} * {num2} = {resultado}")
        case "4":
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
            else:
                resultado = num1 / num2
                print(f"{num1} / {num2} = {resultado}")
	