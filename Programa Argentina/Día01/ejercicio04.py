cadena = input("Ingrese un texto: ")
letra = input("Ingrese una letra: ")


cont = cadena.upper().count(letra.upper())

print("La letra {} se encuentra {} veces en el texto".format(letra,cont))
