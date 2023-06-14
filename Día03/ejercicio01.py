#Resolver ejercicio 12 del Día 2 usando programación de alto nivel

fileFuente = "origen.txt"
fileDestino = "resultado.txt"

fo = open(fileFuente, 'r')
lineas = fo.readlines()

## OPCION1: con ciclos for
cant_palabras = 0
for linea in lineas:
    if len(linea.split()) > cant_palabras:
        lineaTxt = linea
        cant_palabras = len(linea.split())

print(lineaTxt)

## OPCION 2: Usando programacón de alto nivel como plantea el problema
# Usamos la función max para indicar que el criterio de comparación es la
# cantidad de palabras que tiene cada linea y devuleve la que tiene mas palabras

lineaTxt = max(lineas, key=lambda x: len(x.split()))



with open(fileDestino,'w') as wfile:
    wfile.write(lineaTxt)

