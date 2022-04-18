Decimal('1.00') % Decimal('.10')
Decimal('0.00')
1.00 % 0.10
0.09999999999999995

sum([Decimal('0.1')]*10) == Decimal('1.0')
True
sum([0.1]*10) == 1.0
False
""" (decimal)
getcontext().prec = 36
Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
"""