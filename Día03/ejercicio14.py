## EJERCICIO 14: Escribir un programa que determina la lista cuyos elementos resultan en la suma mayor dentro de una lista de listas..

listas_numeros = [[],[3,2],[6,5],[3,2,8],[9,8]]

lista_numeros = max(listas_numeros, key=sum)

print("La lista mayor es {}, igual a: {}".format(lista_numeros,sum(lista_numeros)))
