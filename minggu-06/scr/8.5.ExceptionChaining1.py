try:
     func()
 except ConnectionError as exc:
     raise RuntimeError('Failed to open database') from exc

# output
"""

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
"""