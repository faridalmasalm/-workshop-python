t = Template('Return the $item to $owner.')
 d = dict(item='unladen swallow')
 t.substitute(d)
 #  (Output)
 """
Traceback (most recent call last):

KeyError: 'owner'
 t.safe_substitute(d)
'Return the unladen swallow to $owner.'
"""