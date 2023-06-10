# import math
# n = int(input("Ingrese un numero entero: "))
# print("Calculamos n^2, para n={}: {}".format(n,pow(n,2)))
# print("Calculamos n^3, para n={}: {}".format(n,pow(n,3)))
# print("Calculamos n^n, para n={}: {}".format(n,pow(n,n)))

# Si el usuario ingresa por teclado un numero no entro como un caracter se produce un error
# podemos evitar que se interrumpa la ejecución del programa captuarndo el error y mostrando 
# un mensaje notificando que se ha introducido un valor no entero

try:
    n = int(input("Ingrese un numero entero: "))
    print("Calculamos n^2, para n={}: {}".format(n,n**2))  # equivalente a pow(n,2)
    print("Calculamos n^3, para n={}: {}".format(n,n**3))  # equivalente a pow(n,3)
    print("Calculamos n^n, para n={}: {}".format(n,n**n))  # equivalente a pow(n,n)
except ValueError:
    print("Se produjo un erro de ingreso: Debe introducir un número entero")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
