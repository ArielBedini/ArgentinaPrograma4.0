## Leemos a tupla desde un archivo llamado tupos.txt que contiene un listado de 
## números enteros separados por comas
cadena = ""
archivo_origen = "tupla.txt"
file = open(archivo_origen,'r')
tupla = tuple(file.readline().split(','))
# tupla = (1,4,3,3,5,6)
# Opcion 1
cadena = str(tupla).replace("', '", "").removeprefix("('").removesuffix("')")
# cadena = str(tupla).replace(", ", "").removeprefix("(").removesuffix(")")

# Opción 2 funciona de forma más optima que que funciona con tuplas de cadenas o numeros
print(cadena)
cadena = ""
for elemento in tupla:
    cadena += str(elemento)

print(cadena)
# Opción 3: Utilizando programación de alto nivel
print("El resultado de unir todos los elementos de la tupos es: ","".join(str(x) for x in tupla))
