numeros = input("Ingrese tres numeros enteros separados por comas: ").split(",")


if(len(numeros) != 3):
    print("Debe ingregar exactamente tres numeros enteros separados por comas")
else:
    try:

        suma = numeros[0] + numeros[1] + numeros[2]
        if suma > 10 and suma != 15:
            suma *= 3
        
        print("El resultado es: ", suma)
    except:
        print("Los números ingresados deben ser enteros")