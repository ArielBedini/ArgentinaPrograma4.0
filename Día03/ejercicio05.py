
#lista = ['2', '6', '8', '54', '23', '65', '766', '12', '34', '76', '83', '3']
#lista_numeros = [int(x) for x in lista]

def eliminar_tuplas_vacias(lista):
    for tupla in lista:
        if tupla == ():
            lista.remove(tupla)


lista_tuplas = [(2, 6), (8, 54, 23), (), (65,), (), (766, 12), (), (34,), (76, 83), (3, 2), ()]

print("Opcion 1: Usando ciclos for")
print("Listado Original:")
print(lista_tuplas)
eliminar_tuplas_vacias(lista_tuplas)
print("Lista con tuplas vacias eliminadas:")
print(lista_tuplas)
print()
## Usando Programación de ALto Nivel
print("Opcion 2: Usando programaciónd el alto nivel")
lista_tuplas = [(2, 6), (8, 54, 23), ('',), (65,), (), (766, 12), (), (34,), (76, 83), (3, 2), ()]
print("Listado Original:")
print(lista_tuplas)
print("Lista con tuplas vacias eliminadas:")
print([x for x in lista_tuplas if x != ()])
print("\nVemos otra opción utilizando la función lambda")
print(list(filter(lambda x: len(x)>0, lista_tuplas)))
