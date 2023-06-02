numeros = []
mayor = -1
print("Ingrese diez números enteros")
for i in range(1,11):
    noentero = True
    while noentero:
        try:
            numeros.append(int(input("Ingrese el Nro. {}: ".format(i))))
            noentero = False
        except ValueError:
            print("Debe ingresar números enteros")
            noentero = True
    if numeros[i-1]%2 == 0 and numeros[i-1] > mayor:
        mayor = numeros[i-1]

if mayor != -1:
    print("El mayor valor entero par positivo ingresasdo es: " + str(mayor))
else:
    print("No se ingreso ningún valor entero par positivo")
