#!/usr/bin/env python
#_*_ coding: utf8 _*_

##      Determinar si un número es primo      ##

## Ejemplo 1: llamaremos una función a la cual pasaremos el número a comprobar y nos
## devolverá True o Flase si el número es primo o no, respectivamente...
def esPrimo(num):
    if all(num % y != 0 for y in range(2,num-1)):
        return True
    else:
        return False

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
import math
num = int(input("Ingrese un número: "))
#print(num,"es un mumero primo? ",esprimo(num))
maximo = math.ceil(math.sqrt(num))
if(maximo > 2):
    print([num % y for y in range(2,maximo-1)])
    print(num,"es un número primo? ", all(num % y for y in range(2,maximo-1)))



#primos = [x for x in range(2,1000) if all(x % y != 0 for y in range(2,x-1))]
#print (primos)