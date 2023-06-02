## Pasar numero a su binario

def binario(n):
    if n <= 1:
        return n
    else:
        return str(binario(n//2)) + str(n % 2)


num = int(input("Ingrese un número entero"))


print(binario(num))
