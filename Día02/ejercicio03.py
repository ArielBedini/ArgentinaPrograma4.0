## EJERCICIO 3: Escribir una función que obtenga la suma de los dígitos de un número
## entero no negativo.

def suma_digitos(numero):
    if(numero >= 0):
        if(numero < 10):
            return numero
        else:
            return numero % 10 + suma_digitos(numero // 10)
    else:
        print("El numero debe ser un entero no negativo")

numero = int(input("Ingrese un número entero no negativo: "))
suma = suma_digitos(numero)
if(suma != None):
    print("La suma de los dígitos del número {} es igual a: {}".format(numero,suma))


