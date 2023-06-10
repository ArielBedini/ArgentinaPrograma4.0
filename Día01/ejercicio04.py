cadena = input("Ingrese un texto: ")
letra = input("Ingrese una letra: ")
count = 0
for unaletra in cadena:
    if unaletra == letra:
        count += 1
    

print("La letra {} se encuentra {} veces en el texto".format(letra,count))


print("La letra {} se encuentra {} veces en el texto".format(letra,cadena.count(letra)))
