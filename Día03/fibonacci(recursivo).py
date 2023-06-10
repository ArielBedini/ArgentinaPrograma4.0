def fiborecursivo(n):
    if n < 1:
        return None
    elif n < 3:
        return 1
    return (fiborecursivo(n-1)+fiborecursivo(n-2))

try:
    num = int(input("Ingrese un número entero positivo: "))
    print(fiborecursivo(num))
except:
    print("Debe ingresar un valor numérico entero")
