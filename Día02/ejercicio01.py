#!/usr/bin/env python
#_*_ coding: utf8 _*_

## Determinar si un número es primo ##
## utilizaremos una función a la cual pasaremos el número a comprobar y nos
## devolverá True o Flase si el número es primo o no, respectivamente
numero_primo = int(input("Ingrese un número primo: "))
if esprimo(numero_primo):
    print("Efectivamente el número {} es primo!.. ".format(numero_primo))
else:
    print("El número que ingreso no es primo.")


#primos = [x for x in range(2,1000) if all(x % y != 0 for y in range(2,x-1))]
#print (primos)


import math
num = int(input("Ingrese un número: "))
#print(num,"es un mumero primo? ",esprimo(num))
maximo = math.ceil(math.sqrt(num))
if(maximo > 2):
    print(num,"es un número primo? ", all(num % y for y in range(2,num-1)))
