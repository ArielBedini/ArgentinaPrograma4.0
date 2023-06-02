#Resolver ejercicio'5 del Día 2 usando programación de alto nivel

fileFuente = "source.txt"
fileDestino = "resultado.txt"

# cantidadPalabras = 0
# with open(fileFuente) as rfile:
#     for linea in rfile.readlines():
#         # contar palabras de linea
#         palabrasLinea = len(linea.split(" "))
#         if palabrasLinea > cantidadPalabras:
#             cantidadPalabras = palabrasLinea
#             lineaTxt = linea

fo = open(fileFuente, 'r')
lineas = fo.readlines()

lineaTxt = max(lineas, lambda x: len(x.split(" ")))

with open(fileDestino,'w') as wfile:
    wfile.write(lineaTxt)
