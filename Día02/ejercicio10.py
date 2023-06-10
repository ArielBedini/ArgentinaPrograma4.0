## ESCRIBIR UN PROGRAMA QUE CALCULE LA DISTANCIA ENTRE DOS PUNTOS EN EL PLANO

## Sean dos puntos en el pl
# 
# 
# ano x, y a los que llamamos punto1(x1,y1) y punto2(x2,y2),
## calcular su distancia...
import math

punto_1 = input("Ingresel el Punto 1 (x,y) del plano: ").split(",")
punto_2 = input("Ingresel el Punto 2 (x,y) del plano: ").split(",")

if len(punto_1) == 2 and len(punto_2) == 2:
    try:
        # if (punto_2[0] == punto_1[0]):
        #     distancia = abs(punto_2[1] - punto_1[1])
        # elif (punto2[1] == punto_1[1]):
        #     distancia = abs(punto_2[0] - punto_1[0])
        # else:  # Calculamos la hipotenusa
        #     # calculo = (abs(punto_2[0] - punto_1[0])**2 + abs(punto_2[1] - punto_1[1])**2)
        for i in range(2):
            punto_1[i] = int(punto_1[i])
            punto_2[i] = int(punto_2[i])
        distancia = math.sqrt(((abs(max(punto_2[0],punto_1[0])-min(punto_2[0],punto_1[0])))**2 
            + (abs(max(punto_2[1],punto_1[1]) - min(punto_2[1],punto_1[1]))**2)))

        print("La distancia entre el punto 1 ({},{}) y el punto 2 ({},{}) es {}".format(punto_1[0],punto_1[1],punto_2[0],punto_2[1],distancia))

    except:
        print("Debe ser numero enteros")
else:
    print("Debe ingresar por cada punto dos números enteros positivos separados por coma... ")

