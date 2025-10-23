# Diccionario para contar los votos
votos = {"Ana": 0, "Luis": 0, "María": 0}

voto = input("Vota por Ana, Luis o María (escribe 'fin' para terminar): ")

while voto != "fin":
    if voto in votos:
        votos[voto] += 1
    else:
        print("Voto no válido.")
    
    voto = input("Vota por Ana, Luis o María (escribe 'fin' para terminar): ")

# Mostrar resultados
print("\nResultados:")
print("Ana:", votos["Ana"])
print("Luis:", votos["Luis"])
print("María:", votos["María"])

# Determinar ganador
if votos["Ana"] > votos["Luis"] and votos["Ana"] > votos["María"]:
    print("Ganó Ana.")
elif votos["Luis"] > votos["Ana"] and votos["Luis"] > votos["María"]:
    print("Ganó Luis.")
elif votos["María"] > votos["Ana"] and votos["María"] > votos["Luis"]:
    print("Ganó María.")
else:
    print("Hay un empate.")
