def invertir_cadena(cadena):
    cadena_invertida = ""
    for i in range(1,len(cadena)+1):
        cadena_invertida += cadena[-i]
    return cadena_invertida



cad1 = input("Ingrese una cadena de texto: ")
cad2 = input("Ingrese otra cadena de texto: ")

 # vamos a invertir las cadenas


print("Ivertimos las cadenas:")
print(invertir_cadena(cad1))
print(invertir_cadena(cad2))




