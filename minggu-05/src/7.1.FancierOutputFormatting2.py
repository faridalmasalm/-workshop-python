s = 'Hello, world.'
str(s)
# 'Hello, world.' (output)
repr(s)
# "'Hello, world.'" (output)
str(1/7)
# '0.14285714285714285' (output)
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
# The value of x is 32.5, and y is 40000... (output)
# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# 'hello, world\n' (output)
# The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
# "(32.5, 40000, ('spam', 'eggs'))" (output)