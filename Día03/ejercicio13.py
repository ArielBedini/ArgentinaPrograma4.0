## Ejercicio 13

dic = lambda lst: {palabra: lst.count(palabra) for palabra in set(lst)}

archivo_fuente = "palabras.txt"
archivo = open(archivo_fuente, 'r')

dic_palabras = dic(archivo.read().split())

print(dic_palabras)
dic_palabras_ordenado = {clave:valor for clave, valor in sorted(dic_palabras.items(), key= lambda item: item[1], reverse=True)}
print(dic_palabras_ordenado)

for clave,valor in dic_palabras_ordenado.copy().items():
    if (valor < 2):
        del(dic_palabras_ordenado[clave])

print(dic_palabras_ordenado)
