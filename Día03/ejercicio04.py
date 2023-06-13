archivo_origen = "tupla.txt"
file = open(archivo_origen,'r')
lista = list(file.readline().split(','))

## Opción 1: usando sentencias For para recorrer la tupla
lista_unicos = []
numero = 4
for cont in range(len(lista)):
    if lista[cont] in lista[0:cont]:
        continue
    else:
        lista_unicos.append(lista[cont])
print("Opción 1:")
print(lista_unicos)

## Opción 2 usando programación de alto nivel  para recorrer la tupla
lista_unicos = []
lista_unicos = [x for i,x in enumerate(lista) if x not in lista[:i]]
# lista_unicos = [x for i, x in enumerate(lista) if x not in lista[:i]]
print("Opción 2:")
print(lista_unicos)

print("\nDevolvemos una lista con los elementos únicos, que no aparecen repetidos en la lista")
print(list(filter(lambda x: lista.count(x) == 1, lista)))