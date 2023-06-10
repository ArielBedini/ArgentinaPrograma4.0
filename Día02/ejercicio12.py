fileFuente = "origen.txt"
fileDestino = "resultado.txt"
lineaTxt = ""


cantidadPalabras = 0
with open(fileFuente) as rfile:
    for linea in rfile.readlines():
        # contar palabras de linea
        palabrasLinea = len(linea.split(" "))
        if palabrasLinea > cantidadPalabras:
            cantidadPalabras = palabrasLinea
            lineaTxt = linea

with open(fileDestino,'w') as wfile:
    wfile.write(lineaTxt)
