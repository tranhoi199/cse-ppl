"""
Document:
"""


import functools
import operator

foldLeft = lambda func, init, seq: functools.reduce(func, seq, init)

foldRight = lambda func, init, seq: functools.reduce(lambda x, y: func(y, x), seq[::-1], init)
foldRight_v2 = lambda func, init, seq: functools.reduce(lambda x, y: func(y, x), reversed(seq), init)

arr = ['1', '2', '3', '4', '5']
print(foldLeft(operator.add, 'Y', arr))
print(foldRight(operator.add, 'Y', arr))
print(foldRight_v2(operator.add, 'Y', arr))

'''
Y12345
12345Y
12345Y
'''