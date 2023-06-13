archivo_palabras = "palabras.txt"

archivo = open(archivo_palabras, "r")
listado_palabras = list(archivo.read().split())

class NoEncontrado(Exception):
    pass

try:
    tamanio = int(input("Ingrese un tamaño de palabra desdeado: "))
    if (tamanio < 0):
        raise ValueError("Ingreso un número negativo")
    palabra_encontrada = next((palabra for palabra in listado_palabras if len(palabra) == tamanio),None)
    if (palabra_encontrada == None):
        raise NoEncontrado("Palabra de longitud no encontrada")
    print("La primer palabra de longitud {} encontrada en la posición {} es '{}'".format(tamanio,listado_palabras.index(palabra_encontrada),palabra_encontrada))
except ValueError:
    print("Debe ingresar un valor entero positivo")
except NoEncontrado as e:
    # Manejo para otras excepciones no esperadas
    print("Ocurrió un error:", str(e))

