numeros = input("Ingrese dos numeros enteros separados por comas que definen el intervalo: ")
numeros = numeros.split(",")

try:
    num1 = int(numeros[0])
    num2 = int(numeros[1])
    ## Encontrar la cantidad de múltimplos de 3 en el intervalor [num1, num2]
    cantidad = 0    
    for i in range(num1,num2):
        if i%3 == 0:
            print(i)
            cantidad += 1
except ValueError:
    print("Debe ingresar números enteros")

print("La cantidad de múltiplos de 3 entre {} y {} es: {}".format(num1,num2,cantidad))
