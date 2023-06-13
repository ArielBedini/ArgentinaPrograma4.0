# EJERCICIO 02

# Solicitamos al usuairo ingrese un número a contar la cantidad
# de ocurrencias dentro de la tupla
archivo_fuente = "tupla.txt"
contador = 0
## Leemos los números dentro de un archivo de texto, separados por comas
## y los convertimos en una tupla

file = open(archivo_fuente, 'r')
## Cómo los numero contenido en un archivo de texto se leen como texto primero
## creamos una lista de numeros de tipo string
lista = list(file.read().split(","))
## luego creamos la tupla pasando cada número string de la lista a su equivalente entero
tupla = tuple(int(num) for num in lista)
print(tupla)
try:
    numero = int(input("Ingrese un numero entero: "))
    # Opción 1: iterando por cada elemento 'x' de la lista incrementando un contador
    # cada vez que (x = numero)
    for x in tupla:
        if x == numero:
            contador += 1

    print ("La cantidad de veces que aparece el número {} en la tupla es de {} veces".format(numero,contador))

    ## Opción 2: utilizando programación de lato nivel
    cantidad = tupla.count(numero)
    print ("La cantidad de veces que aparece el número {} en la tupla es de {} veces".format(numero,cantidad))

except:
    print("Debe ingresar un númeroe entero")

