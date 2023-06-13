## Ejercicio 09

## Recorrer dos listas a al vez

lista_letras = ['a', 'b', 'c', 'd', 'e', 'f']
lista_numeros = [11, 12, 13, 14, 15, 16]

# Opción 1
hasta = min(len(lista_letras),len(lista_numeros))
listaconjunta = [(lista_letras[x], lista_numeros[x]) for x in range(hasta)]
print(listaconjunta)

# Opción 2
for (a,b) in  zip(lista_letras,lista_numeros):
    print(a,b)


# Opción 3
print([x for x in zip(lista_letras,lista_numeros)])

