mayor = -1
for cont in range(10):
    try:
        num = int(input("Ingrese un numero entero: "))
    except:
        print("Debe ingresar un numero entero")
        continue
    if (num % 2 == 0) and (0 < num > mayor):
        mayor = num


print("El mayor número ingresado es ", mayor)


