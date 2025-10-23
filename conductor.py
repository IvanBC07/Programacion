# pedir al usuario la edad
# si la edad esta entre los 18 y los 80, sacaremos el mensaje "puedes tener carnet de conducir"
# si la edad es mayor de 80, sacaremos el mensaje "Ya es hora de que tus hijos te hagan de chofer"


edad = int(input("Ingrese la edad: "))

if 18 <= edad <= 80:
    print("Puedes tener carnet de conducir")

elif edad > 80:
    print("Ya es hora de que tus hijos te hagan de chofer")

else:
    print("Eres menor de edad")