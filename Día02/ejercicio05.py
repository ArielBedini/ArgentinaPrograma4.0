## EJERCICIO 5: Escribir un programa que encuentre el máximo común divisor entre dos números.

def max_com_div(num_1, num_2):
    menor = min(num_1,num_2)
    for i in range(menor,2,-1):
        if(not(num_1 % i) and not(num_2 % i)):
            return i

                    
print("Ingrese dos numeros")
numero_1 = int(input("Número 1: "))
numero_2 = int(input("Número 2: "))

print(max_com_div(numero_1, numero_2))



