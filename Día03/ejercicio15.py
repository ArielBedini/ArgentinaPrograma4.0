## EJERCICIO 15: Escribir un programa que obtenga la profundidad del diccionario:
## dic = {'a':1, 'b':{'c':{'d':{}}}}

dic = {'a':1, 'b':{'c':{'d':{}}}}

##OPCIÓN 1: Con una función recursiva y entro un el un cilo for
def recorre_dict(d):
    for i in d.values():
        if type(i) == dict:
            return 1 + recorre_dict(i)
    return 1

print(recorre_dict(dic))

## OPCION 2: Con un función de alto nivel

def profundidad_dic(d):
    if isinstance(d, dict):
        print("es un diccionario")
        return 1 + (max(map(profundidad_dic,d.values())) if d else 0)
    return 0

print(profundidad_dic(dic))

d1 = {}
print(d1.values())