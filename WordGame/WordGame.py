# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:32:49 2020

@author: Federico
"""

import math
import random
import os

VOCALES = 'aeiou'
CONSONANTES = 'bcdfghjklmnpqrstvwxyz'
TAMANIO_MANO = 7
JUGAR_CON_COMODIN = True
VALORES_LETRAS = {
    '*' : 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'ñ': 4, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}



# -----------------------------------
# Codigo de ayuda
#

ARCHIVO_PALABRAS = "palabras.txt"



def control_pantalla(f, texto = ""):
    """
    Esta función controla la forma en que se presentan mensajes de texto en pantalla de consola, debiante
    la implementación de tres funciones internas.
    Recibe dos argumentos, el primero es el nombre de la función interna a ejecutar y el segundo (opcional)
    es el mensaje de texto que queremos presentar.
    Las funciones internar que podemos ejecutar pasando pasando su nombre como primer parámentro son:
        - limpiar_pantalla()
        - centrar_texto(texto)
        - mostrar_cartel(texto)
    """
    def limpiar_pantalla():
        if os.name == 'nt':  # Para sistemas Windows
            os.system('cls')
        else:  # Para sistemas Unix/Linux/Mac
            os.system('clear')

    def centrar_texto(texto):
        terminal_width = os.get_terminal_size().columns
        espacios = (terminal_width - len(texto)) // 2
        texto_centralizado = " " * espacios + texto
        return texto_centralizado
    
    def mostrar_cartel(texto):
        ancho_texto = len(texto)
        ln2 = centrar_texto("*"*(ancho_texto+4))+"\n"
        ln1 = centrar_texto("*"+" "*(ancho_texto+1)+" *")+"\n"
        ln0 = centrar_texto("*"+" "+texto+" *")+"\n"
        return ln2+ln1+ln0+ln1+ln2

    # verifica que el primer parametro 'f' coincide con uno de los nombres de la funciones internas
    # y procede a a la función correspondiente
    if f == "limpiar_pantalla":
        limpiar_pantalla()
    if f == "centrar_texto":
        return centrar_texto(texto)
    if f == "mostrar_cartel":
        return mostrar_cartel(texto)


def cargar_palabras():
    """
    Retorna una lista de palabras válidas, compuestas por letras en minúscula.
    
    Dependiendo del tamaño de la lista de palabras, esta función puede tomarse su tiempo para finalizar.
    """
    
    print("Cargando lista de palabras desde el archivo...")
    # inFile: Archivo
    inFile = open(ARCHIVO_PALABRAS, 'r')
    # palabras: lista de cadenas
    palabras = []
    for palabra in inFile:
        palabras.append(palabra.strip().lower())
    print("  ", len(palabras), "palabras cargadas.")
    return palabras

def obtener_diccionario_frecuencias(secuencia):
    """
    Genera un diccionario donde las claves son los elementos de la secuencia
    y los valores son enteros, que indican la cantidad de veces que ese
    elemento está repetido en la secuencia.

    secuencia: cadena o lista
    return: diccionario {tipo_elemento -> int}
    """
    
    # frecuencias: diccionario
    frec = {}
    for x in secuencia:
        frec[x] = frec.get(x,0) + 1
    return frec
	
#
# (fin Codigo de ayuda)
# -----------------------------------

#
# Problema #2: Puntuar una palabra
#
def obtener_puntaje_palabra(palabra, n):
    """
    Obtiene el puntaje de una palabra. Asume que la palabra es una palabra válida.

    Podemos asumir que la palabra siempre será una cadena de letras 
    o la cadena vacía (""). No se puede asumir que solo contendrá letras en
    minúsculas, así que deberemos resolver también con palabras con letras en
    mayúscula y minúscula.
    
	El puntaje de una palabra es el producto de dos componentes:

	Primer componente: la suma de los puntos de las letras en la palabra.
    Segundo componente: 1 o la fórmula 
        [7 * longitud_palabra - 3 * (n - longitud_palabra)], el valor que 
    sea más grande, donde longitud_palabra es la cantidad de letras usadas 
    en la palabra y n es la cantidad de letras disponibles en la mano actual.

    Al igual que en Scrabble, cada letra tiene un puntaje.

    palabra: cadena
    n: int >= 0
    retorna: int >= 0
    """
    ## Paa trabajar con 'palabra'haremos lo siguiente en todas las funcines:
    ## pasaremos palabra a minsculas  y eliminaremos los espacios anteriores y 
    ## posterioes a la palabra y los que pueda haber entre letras
    palabra = palabra.lower().replace(" ","")

    primera_componente = sum(VALORES_LETRAS[x] for x in palabra)
    segunda_componente = max(1,(7 * len(palabra) - 3 * (n - len(palabra))))

    return primera_componente * segunda_componente



def mostrar_mano(mano):
    """
    Muestra las letras que están en la mano del jugador.

    Por ejemplo:
       mostrar_mano({'a':1, 'x':2, 'l':3, 'e':1})
    Debería mostrar por consola lo siguiente:
       a x x l l l e
    El orden de las letras no es importante.

    mano: diccionario (string -> int)
    """
    
    for letra in mano.keys():
        for j in range(mano[letra]):
             print(letra, end=' ')      # Muestra todas las letras en la misma linea
    print()                             # Linea vacía


def repartir_mano(n):
    """
    Genera una mano al azar con n letras en minúscula.
    techo(n/3) letras en la mano deben ser VOCALES.

    Las manos se representan como diccionarios. Las claves son letras 
    y los valores indican el número de veces que esa letra está contenida 
    en la mano.

    n: int >= 0
    Retorna: diccionario (string -> int)
    """
    
    mano={}

    ## Agregue un incremento al número de vocales porque al aumentar TAMANIO_MANO no me convence la cantidad de vocales con las que podemos jugar
    if not (n % 3): ## si es múltimplo de 3
        inc = 1
    else:
        inc = 0

    ## 

    cantidad_vocales = int(math.ceil(n / 3)) + inc

    for i in range(cantidad_vocales):
        x = random.choice(VOCALES)
        mano[x] = mano.get(x, 0) + 1
    
    for i in range(cantidad_vocales, n):    
        x = random.choice(CONSONANTES)
        mano[x] = mano.get(x, 0) + 1

    if JUGAR_CON_COMODIN:
        vocal_a_reemplazar = random.choice(list(x for x in VOCALES if x in mano))
        if mano[vocal_a_reemplazar] > 1:
            mano[vocal_a_reemplazar] -= 1
        else:
            del(mano[vocal_a_reemplazar])
        mano['*'] = 1

    return mano

#
# Problema #3: Actualizar la mano eliminando letras.
#
def actualizar_mano(mano, palabra):
    """
    NO asumir que la mano contiene el mismo número de veces una letra 
    que las que aparece en la palabra. Las letras que están en la palabra 
    y no en la mano deben ser ignoradas. Las letras que aparecen más veces 
    en la palabra que en la mano no deben resultar en un total negativo; 
    debemos eliminar esa letra de la mano o poner su cantidad en 0.

    Actualiza la mano: usa las letras que están en la palabra y retorna 
    la nueva mano, sin esas letras.

    No debe modificar mano, sino que debe retornar un nuevo diccionario.

    palabra: string
    mano: diccionario (string -> int)    
    retorna: diccionario (string -> int)
    """

    ## Paa trabajar con 'palabra'haremos lo siguiente en todas las funcines:s
    ## pasaremos palabra a minsculas  y eliminaremos los espacios anteriores y 
    ## posterioes a la palabra y los que pueda haber entre letras
    palabra = palabra.lower().replace(" ","")

    nueva_mano = mano.copy()
    for letra in palabra:
        if letra in nueva_mano:
            if nueva_mano[letra] == 1:
                del(nueva_mano[letra])
            else:
                nueva_mano[letra] -= 1

    return nueva_mano

    
#
# Problema #4: Verificar si la palabra es válida.
#
def es_palabra_valida(palabra, mano, lista_palabras):
    """
    Devuelve True si la palabra está en lista_palabras y está compuesta
    completamente por letras en la mano. Sino, devuelve False.
    No se debe modificar ni mano ni lista_palabras.
   
    palabra: string
    mano: diccionario (string -> int)
    lista_palabras: lista de cadenas en minúsculas
    Retorna: boolean
    """
    
    ## Paa trabajar con 'palabra'haremos lo siguiente en todas las funcines:s
    ## pasaremos palabra a minsculas  y eliminaremos los espacios anteriores y 
    ## posterioes a la palabra y los que pueda haber entre letras
    palabra = palabra.lower().replace(" ","")
    
    palabra_frecuencias = obtener_diccionario_frecuencias(palabra)
    # if all(letra in mano.keys() for letra in palabra) and all(palabra_frecuencias[letra] <= mano[letra] for letra in palabra_frecuencias):
    if all(letra in mano.keys() and palabra_frecuencias[letra] <= mano[letra] for letra in palabra_frecuencias):
        palabras = list(palabra.replace('*', vocal) for vocal in VOCALES)
        return any(una_palabra in lista_palabras for una_palabra in palabras)
    return False
    """
    palabra = palabra.lower() # pasamos la palabra a minúsculas
    ## condición: cada letra de la palabra que ingreso el jugardor existe en la mano actual ???
    ## pero cuidado porque la condición anterior no detecta palabra inválida si palabra="holaaaa" y mano=['a','h','o','l']
    ## para este caso tenemos que verificar la cantidad de veces que tenemos cada letra en palabra y 
    ## compararla con la mano, para ello usamos la función que ya viene definida: "obtener_diccionario_frecuencias"
    palabra_frecuencias = obtener_diccionario_frecuencias(palabra)
    for letra in palabra_frecuencias:
        if not(letra in mano.keys() and palabra_frecuencias[letra] <= mano[letra]):
            ## si existe al menos una letra de la palabra que no este en la mano o 
            ## si el número de veces que aparece la letra en palabra es mayor al de la mano
            ## entonces la palabra no es váĺida
            return False 
    ## si llegamos hasta acá la palara es valida, pero si jugamos con comodines tenemos que hacer
    ## un par de cosas más..

    ## primero creamos una lista con las palabras que se forman reemplazando el asterisco con cada vocal
    palabras = list(palabra.replace('*', vocal) for vocal in VOCALES)
    ## lo bueno de esto es que funciona igual si jugamos o no con asteriscos, cualquiera fuera el caso la lista palabras 
    ## contendrá todas las variantes que se obtiene al reemplazar el asterisco por cada vocal o al menos contendrá 
    ## palabra (original) unicamante si no jugamos con asteriscos, ya que la funcion remplace() no encuantra un asterico para reemplazar....

    ## luego buscamos cualquier coincidencia de la/s palabra/s dentro de lista_palabras y si existe al menos una,
    ## la primera que encuantre, devuelve True, caso contrario si no encuentra una coincidencia devolverá False
    return any(una_palabra in lista_palabras for una_palabra in palabras)
    """






#
# Problema #5: Jugar una mano
#
def calcular_longitud_mano(mano):
    """ 
    Retorna la longitud (cantida de letras) en la mano actual.
    
    mano: diccionario (string-> int)
    retorna: integer
    """
    return sum(mano.values())



def jugar_mano(mano, lista_palabras, repetir_mano):

    """
    Permite que un usuario juegue una mano, con las siguientes consideraciones:

    * Se le muestra la mano actual.
    
    * El usuario puede ingresar una palabra.

    * Cuando una palabra es ingresada (válida o inválida), utiliza letras de la mano.

    * Una palabra inválida se rechaza, mediante un mensaje que le pide al usuario
      que ingrese otra palabra.

    * Después de cada palabra válida: se muestra el puntaje de la palabra, 
      las letras restantes de la mano y se le pide al usuario que ingrese 
      otra palabra.

    * La suma de los puntajes de las palabras se presenta una vez que la mano termina.

    * La mano termina cuando no hay más letras sin usar.
      El usuario también puede terminar la mano ingresando dos signos de exclamación
      ('!!') en vez de una palabra.

      mano: diccionario (string -> int)
      lista_palabras: lista de cadenas en minúsculas.
      retorna: el puntaje total de la mano
      
    """
    
    # PSEUDO-CODIGO
    # Llevar registro del puntaje total
    
    # Mientras haya letras en la mano o el usuario no ingrese '!!':
    
        # Mostrar la mano
        
        # Pedirle al usuario que ingrese una palabra
        
        # Si la entrada son dos signos de exclamación, se termina el juego
                    
        # Sino (la entrada no son dos signos de exclamación):

            # Si la palabra es válida:

                # Mostrarle al usuario los puntos que ganó,
                # y el puntaje total de la mano hasta ese momento.

            # Sino (la palabra no es válida):
                # Rechazar palabra inválida (mostrar un mensaje)
                
            # actualizar la mano del usuario eliminando las letras 
            # que usó en la palabra (aún si la palabra era inválida)
            

    # Se terminó el juego (el usuario se quedó sin letras o ingresó '!!'),
    # se le muestra el puntaje final de la mano.

    # Retorna el puntaje final como resultado de la función.
    puntaje_mano = 0
    intercambiar_letra = False

    ## creamos una copia de la mano con la cual haremos los cambios
    mano_a_jugar = mano.copy()

    ## Este ciclo se repite mietras queden letras en la mano o el usuario no finalice la mano
    while len(mano_a_jugar) > 0:
        print("Mano actual:",end=" ")
        mostrar_mano(mano_a_jugar)
        
        if not intercambiar_letra and not repetir_mano:
            intercambiar_letra = True
            print ()
            intercambiar = input(control_pantalla("centrar_texto","-> Desear cambiar una letra? [S=Si/N=No]: ")).replace(" ", "")
            print()
            if intercambiar.upper() == 'S' or intercambiar.upper() == 'SI':
                letra_a_intercambiar = input(control_pantalla("centrar_texto","-> Ingrese la letra a intermbiar: "))
                mano_a_jugar = intercambiar_mano(mano_a_jugar,letra_a_intercambiar)
                print("Mano actual:",end=" ")
                mostrar_mano(mano_a_jugar)

        ## Pedimos al jugador que ingrese una palabra
        palabra = input(control_pantalla("centrar_texto","-> Ingrese una palabra o '!!' para finalizar: "))
        palabra =  palabra.lower().replace(" " , "")
        if palabra == "!!":
            break
        if es_palabra_valida(palabra, mano_a_jugar, lista_palabras):
            puntaje_palabra = obtener_puntaje_palabra(palabra, len(mano_a_jugar))
            puntaje_mano += puntaje_palabra
            print("{} resulta en {} puntos. Total {}".format(palabra,puntaje_palabra,puntaje_mano))
        else:
            print("'{}' no es una palabra válida".format(palabra))

        mano_a_jugar = actualizar_mano(mano_a_jugar, palabra)
    
    return puntaje_mano



#
# Problema #6: Jugar una partida completa
# 


#
# procedimiento para reemplazar una letra en la mano
#

def intercambiar_mano(mano, letra):
    """
    Permite al usuario reemplazar todas las copias de una letra en la mano 
    (elegida por el usuario) por una nueva letra elegida, al azar, de VOCALES 
    y CONSONANTES. La nueva letra debe ser diferente a la elegida para intercambiar, 
    y no puede ser ninguna de las letras que ya tiene en la mano.
    
    Si el usuario ingresa una letra que no está en la mano, la mano debe quedar igual.
    
    No se debe modificar la mano original.
    Por ejemplo:
        intercambiar_mano({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    puede resultar en:
        {'h':1, 'e':1, 'o':1, 'x':2} -> si la nueva letra es 'x'
    La nueva letra no debe ser 'h', 'e', 'l', u 'o' ya que esas letras ya están en 
    la mano.
    
    mano: diccionario (string -> int)
    letra: string
    retorna: diccionario (string -> int)
    """

    ## Para trabajar con la letra ingresada por el usuario:
    ## primero pasaremos la letra a minsculas  y eliminaremos los espacios anteriores y 
    ## posterioes
    letra = letra.lower().replace(" ","")


    if JUGAR_CON_COMODIN and letra == "*":
        print ("\nEl comodín no se puede intercambiar!!\n")
        return mano
    letra_repetida = True
    if letra in mano.keys():
        while letra_repetida:
            nueva_letra = random.choice(VOCALES+CONSONANTES)
            letra_repetida = nueva_letra in mano.keys()
        mano[nueva_letra] = 1
        if mano[letra] > 1:
            mano[letra] -= 1
        else:
            del(mano[letra])
    else:
        print("\nLa letra ingresada no está en la mano!!\n")
    
    return mano

#
# Problema #1: Armar esqueleto del ciclo de juego
#       
    
def jugar_partida(lista_palabras):
    """
    Permitir al usuario jugar una serie de manos (partida)

    * Pedir al usuario que ingrese un número total de manos.

    * Acumular el puntaje de cada mano en un puntaje total para la partida.
 
    * Por cada mano, antes de empezar a jugar, preguntar al usuario si quiere
      intercambiar una letra por otra. Esto se puede hacer sólo una vez durante 
      el juego. Una vez que se usa esta opción, no se le debe preguntar nuevamente 
      al usuario si quiere intercambiar una letra durante el juego.
    
    * Por cada mano, preguntar al usuario si desea volver a jugar la mano.
      Si el usuario ingresa 'si', se repetirá la mano y se mantendrá el mayor
      de los dos puntajes obtenidos para esa mano. Esto se puede hacer una única vez
      durante la partida. Una vez que se utiliza la opción de volver a jugar una mano,
      no se debe volver a preguntar si desea volver a jugar futuras manos. Volver a
      jugar una mano no afecta el número de manos totales que el usuario eligió jugar.
      
            * Nota: si se vuelve a jugar una mano, no se podrá elegir reemplazar una
              letra (se debe jugar con la mano original)
      
    * Devuelve el puntaje total de la partida.

    lista_palabras: lista de cadenas en minúsculas
    """
    
        
    ##! Ciclo del Juego
    ## Inicializar variables de control
    manos_jugadas = 0
    puntaje_juego = 0
    numero_de_manos_correcto = False
    quedan_manos_por_jugar = False
    repetir_mano = False



    ## Personalizamos el error en el ingreso de la cantidad de patidas a jugar
    class NumeroNegativo(Exception):
        pass

    ## Iniciamos el ciclo de control de ingreso de un valor entero positvo por parte del usuario
    ## Si el número de manos a juagar es 0 se sale del juego!
    print()
    while not numero_de_manos_correcto:
        print(control_pantalla("mostrar_cartel", "¡¡  B i e n v e n i d o   a   W O R D  G A M E  !!"))
        try:
            cantidad_manos = int(input(control_pantalla("centrar_texto", "-> Ingrese el número de manos a jugar (0 para salir): ")))
            numero_de_manos_correcto = cantidad_manos >= 0
            if cantidad_manos < 0:
                raise NumeroNegativo("\nDebe ingresar numeros positivos")
            if cantidad_manos == 0:
                print("\n"+control_pantalla("centrar_texto","¡¡ Saliste de WordGame, ... te esperamos pronto para un nuevo desafío !!")+"\n")
                continue
        except ValueError:
            control_pantalla("limpiar_pantalla","")
            print("\nDebe ingresar un número entero")
        except NumeroNegativo as e:
            control_pantalla("limpiar_pantalla","")
            print(e)
            continue

    quedan_manos_por_jugar = cantidad_manos != 0

    ## Inicio del Ciclo del Juego: "mientras quede manos por jugar"
    while quedan_manos_por_jugar:
        puntaje_mano = [0]
        print()
        txt_titulo = "*** Jugando Mano Nro.: " + str(manos_jugadas+1) + " ***"
        print(control_pantalla("centrar_texto",txt_titulo))
        print()
        mano = repartir_mano(TAMANIO_MANO)
        ## Este ciclo se repite unicamante si se velve a jugar la mano
        while True:
            puntaje_mano.append(jugar_mano(mano, lista_palabras, repetir_mano))
            # txtrepetir = ""
            # if repetir_mano:
            #     txtrepetir = "repetida"
            # print("Puntaje final de la mano Nro. {} {}: {}".format(manos_jugadas+1,txtrepetir,puntaje_mano[len(puntaje_mano)-1]))
            if not repetir_mano:
                print()
                repetir = input(control_pantalla("centrar_texto","... Desea repetir la mano? [S=Si/N=No]: "))
                print()
                repetir_mano = repetir.upper() == 'S' or repetir.upper() == 'SI'
                if not repetir_mano:
                    break
            else:
                break

        # if repetir_mano:
        #     print("Puntaje final de la mano Nro. {} es: {}\n".format(manos_jugadas+1, max(puntaje_mano)))
            
        puntaje_juego += max(puntaje_mano)
        manos_jugadas += 1
        quedan_manos_por_jugar = cantidad_manos > manos_jugadas
    
    if cantidad_manos > 0:
        txt_titulo = "Puntaje final obtenido en {} mano/s: {}".format(cantidad_manos, puntaje_juego)
        print()
        print(control_pantalla("mostrar_cartel",txt_titulo))
        print()




        
#
# Construye las estructuras de datos necesarias para jugar la partida.
# No eliminar la condición "if __name__ == '__main__':" Este código se ejecuta
# cuando el programa se ejecuta directamente, sin usar la sentencia import.
#
if __name__ == '__main__':
    control_pantalla("limpiar_pantalla")
    lista_palabras = cargar_palabras()
    jugar_partida(lista_palabras)
    
