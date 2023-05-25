cadena1 = input("Ingrese una cadena de texto: ")
cadena2 = input("Ingreses otra cadena de texto: ")

print(cadena2+ " "+ cadena1)

cadena1 = cadena1[::-1]
cadena2 = cadena2[::-1]
print(cadena2 + " " + cadena1)

#En este ejemplo, utilizamos el operador de rebanado [::-1] para invertir la cadena. El operador [::-1] indica que queremos una rebanada que abarque desde el principio hasta el final de la cadena, pero con un paso de -1, lo que implica que se recorra la cadena en orden inverso.

