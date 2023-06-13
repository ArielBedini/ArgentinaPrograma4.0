lista_numeros = [2, 6, 8, 54, 23, 65, 766, 12, 34, 76, 83, 3]
lista_numeros.sort()
print(lista_numeros)
try:
    rango = input("Ingrese dos números separados por comas: ")
    rango = rango.split(",")
    mayor = int(max(rango)) + 1
    menor = int(min(rango)) 
    print(range(menor,mayor))
    cantidad = len(list(filter(lambda num: num in lista_numeros, range(menor,mayor))))
    print(cantidad)
except ValueError:
    print("Debe ingresar valores enteros")