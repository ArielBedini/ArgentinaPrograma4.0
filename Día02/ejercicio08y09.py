## Escribir un programa que obtenga el año, el número de semana y el día actual

import datetime

## obtenemos la fecha actual en formato YYYY-mm-dd
fecha_actual = datetime.date.today()

## Obtener el año
anio_actual = fecha_actual.year
print("El año actual es:",anio_actual)

## Obtener el número de semana
semana_actual = fecha_actual.isocalendar()[1]
## Ten en cuenta que el método isocalendar() devuelve una tupla con tres valores: el año, el número de semana y el día de la semana
## (donde el lunes es el día 1 y el domingo es el día 7).
print("La semana actual es:",semana_actual)

## Obtener el día actual
dia_semana_actual = fecha_actual.isocalendar()[2]
print("El día de la semana:",dia_semana_actual)