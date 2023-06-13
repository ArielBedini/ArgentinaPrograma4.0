##EJERCICIO 12: Mostrar los valores unicos dentro de un diccionario

diccionario = {
    "manzana": 3,
    "plátano": 5,
    "naranja": 2,
    "pera": 4,
    "uva": 8,
    "kiwi": 6,
    "mango": 2,
    "piña": 3,
    "sandía": 5,
    "melón": 2
}

tupla = tuple(diccionario.values())
unicos = list(filter(lambda x: tupla.count(x)==1, tupla))
print("Los valores únicos del diccionario son: ", unicos)

conjunto = list(set(diccionario.values()))  ## Usamo list para ajcer uniformes las salidas
print("Mostramos todos los valores de dicionario sin repetirse: ",conjunto)
