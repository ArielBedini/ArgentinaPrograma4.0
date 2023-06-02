from decimal import Decimal
x = 0.0
for i in range(10):
    x = Decimal(x) + Decimal('0.1')

if x == 1.0:
    print(x, 'es igual a 1.0')
else:
    print(x, 'no es igual a 1.0')