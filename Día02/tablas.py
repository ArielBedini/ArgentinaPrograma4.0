# Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)

# tabla = [[":(", ":)", ":(", ":)"],
#         [":)", ":(", ":)", ":)"],
#         [":(", ":)", ":)", ":("],
#         [":)", ":)", ":)", ":("]]
# tabla = [[elemento[((y + x) % 2)] for y in range(4)] for x in range(4)] ## no funciona

tupla_elemento = ":(",":)" 
## Como la disposición de los elementos en la tabla es aletoria y no sigue
## un patron determinado podemos utilizar un sistema de ubicación con referencia
## al indice de cada elemento dentro de la tupla_elementos la cual podemos considerarala
## una tupla binaria ya que posee dos elementos disntios en las posición 0 y 1...
## Por lo tanto podemos expresar la disposición de los elementos en la tabla de la 
## siguiente forma

tabla_binaria = '0101101101101110'
binario =int(tabla_binaria,2) & (2**0)
# tabla = [[tupla_elemento[int(tabla_binaria,2) & (2**(x+y))] for x in range(4)] for y in range(0,12,4)]
tabla = [[tupla_elemento[int(tabla_binaria[x+y])] for x in range(4)] for y in range(0,15,4)]

# print([[int(tabla_binaria,2) & (2**(x+y)) for x in range(4)] for y in range(0,12,4)])
print(tabla)

