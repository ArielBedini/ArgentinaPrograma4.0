## Escribir un programa que obtenga la fecha actual en Python.

import datetime

fecha_actual = datetime.date.today()

## imprime la fecha en el formato año-mes-dia
print(fecha_actual)

## utilizamos el método strftime para dar el formato deseado a la fecha
print(fecha_actual.strftime("%d/%m/%Y"))

