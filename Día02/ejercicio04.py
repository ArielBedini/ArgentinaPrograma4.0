## EJERCICIO 04: Escribir un programa que calcule el valor de ‘a’ a la potencia de ‘b’.
import math

base = int(input("Ingrese un valor: "))
exponente = int(input("Ingrese el exponente: "))

print("El numero {} elevado a la potencia de {} es igual a: {}".format(base,exponente,int(math.pow(base,exponente))))
