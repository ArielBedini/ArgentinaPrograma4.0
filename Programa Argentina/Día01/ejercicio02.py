lista = input("Ingrese tres valores enteros (a,b,c) separados por coma: ")
lista = lista.split(",")

if(len(lista) != 3):
    print("Debe ingregar exactamente tres numeros enteros separados por comas")
else:
    try:
        a = int(lista[0])
        b = int(lista[1])
        c = int(lista[2])

        print("Determinar si a=2*b, para a={} y b={}".format(a,b))
        condicion = ""
        if(a != b*2):
            condicion = "no"
        print("Esta condicion {} se cumple!, ya que {} {} es igual a {}".format(condicion, a , condicion, b*2))


        print("Determinar si b=a*c")
        condicion = ""
        if(b != a*c):
            condicion = "no"
        print("Esta condicion {} se cumple!, ya que {} {} es igual a {}".format(condicion, b , condicion, a*c))

        print("Determinar si c=b/a")
        condicion = ""
        if(c != b/a):
            condicion = "no"
        print("Esta condicion {} se cumple!, ya que {} {} es igual a {}".format(condicion, c , condicion, b/a))

    except ValueError:
        print("Error: debes introducior valores enteros")
