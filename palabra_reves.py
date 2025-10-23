palabra = str(input("Ingrese una palabra: "))


invertida = ""

for letra in palabra:
    invertida = letra + invertida

print("La palabra invertida es:", invertida)