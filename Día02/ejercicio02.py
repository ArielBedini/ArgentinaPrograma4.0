
## EJERCICIO 2: Escribir una función que verifique si una cadena dada es un palíndromo,
## es decir, se lee de la misma manera hacia adelante y hacia atrás.
import math
def palidromo(palabra):
    long = len(palabra)
    # media_long = math.ceil(long) // 2
    if long<=2:
        return False
    else:
        return all(palabra[i] == palabra[long-i-1] for i in range(0,(long//2)+1))

palabra = input("Ingrese una palabra: ")
print(palabra," es un palidromo?: ", palidromo(palabra))
