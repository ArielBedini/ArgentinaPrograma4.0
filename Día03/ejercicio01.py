#Resolver ejercicio'5 del Día 2 usando programación de alto nivel

fileFuente = "source.txt"
fileDestino = "resultado.txt"

fo = open(fileFuente, 'r')
lineas = fo.readlines()

lineaTxt = max(lineas, lambda x: len(x.split(" ")))

with open(fileDestino,'w') as wfile:
    wfile.write(lineaTxt)
