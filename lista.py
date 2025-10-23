lista1 = [1,2,3,4,5,6,7,8]


print ("Mi lista tiene", len(lista1), "elementos")
print ("El elemento 4 de mi lista es: ", lista1[3])

print("Lista antes de añadir un nuevo valor" , lista1)

lista1.append(9)
print("Lista despues de añadir el nuevo valor", lista1)

lista1.remove(lista1[4])
print ("lista despues de eliminar el elemento de orden 4 ", lista1)