try:
     raise NameError('HiThere')
 except NameError:
     print('An exception flew by!')
     raise

# output
"""
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
"""