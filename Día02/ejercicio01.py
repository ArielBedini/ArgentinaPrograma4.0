#!/usr/bin/env python
#_*_ coding: utf8 _*_


## EJERCICIO 1: Escribir una función que determine si un número entero es primo. ###

import math
## Ejemplo 1: llamaremos una función a la cual pasaremos el número a comprobar y nos
## devolverá True o Flase si el número es primo o no, respectivamente...
def esPrimo(num):
    return all(num % y for y in range(2,num-1))
    
def es_primo(numero):
    if numero < 2:
        return False

    # Calcular la raíz cuadrada del número
    limite = int(math.sqrt(numero)) + 1

    # Verificar divisibilidad por todos los números hasta la raíz cuadrada
    for i in range(2, limite):
        if numero % i == 0:
            return False

    return True


numero_primo = int(input("Ingrese un número primo: "))
if esPrimo(numero_primo):
    print("Efectivamente el número {} es primo!.. ".format(numero_primo))
else:
    print("El número que ingreso no es primo.")



## Ejemplo 2: utilizaremos las funciones predefinidas en el módulo math
## math.ceil() devolverá un entero igual o mayor más práximo al número dado
## math.sqrt() obtenemos la ráiz cuadrada del número ya que para comprobar si
## es primo solamente es nececeario buscar divisores desde el número 2 hasta 
## la mitad del número dado.
## La función all() toma un iterable como argumento y retorna True solo si todos
## los elementos del iterable tienen un valor booleano de True o el iterable está 
## vacío, en los demás casos retornara False

num = int(input("Ingrese un número primo: "))
# Consideremos un número compuesto N y supongamos que tiene dos factores, a y b, 
# tales que a * b = N. Si ambos factores fueran mayores que la raíz cuadrada de N, entonces su producto (a * b) sería mayor que N, 
# lo cual es una contradicción, ya que estamos asumiendo que a * b = N. Por lo tanto, al menos uno de los factores debe ser menor 
# o igual que la raíz cuadrada de N.
# Basándonos en esta propiedad, cuando queremos verificar si un número N es primo, solo necesitamos verificar si existe algún 
# factor primo menor o igual que su raíz cuadrada. Si no se encuentra ningún factor primo en ese rango, entonces el número N es primo.
# Este enfoque ayuda a reducir el número de comprobaciones necesarias y mejora el rendimiento del algoritmo de verificación de primos.



def ver_si_es_primo(numero):
    if numero < 2:
        return False

    # Calcular la raíz cuadrada del número
    maximo = math.ceil(math.sqrt(num)) + 1  ## tambien podemos usar la formula: int(math.sqrt(num))+1
    return  all(num % y for y in range(2,maximo))

if(ver_si_es_primo(num)):
    print("El número {} es primo!!".format(num))
else:
    print("{} NO es primo!!".format(num))


# primos = [x for x in range(2,1000) if all(x % y != 0 for y in range(2,x-1))]
# print (primos)
