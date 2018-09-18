import functools
import operator


arr = ['a', 'b', 'c', 'd', 'e']

print(functools.reduce(lambda x, y: x + y, arr))
'''
abcde
'''

print(functools.reduce(lambda x, y: y + x, arr))
'''
edcba
'''

print(functools.reduce(lambda x, y: x + y, arr, 'Y'))
'''
Yabcde
'''

print(functools.reduce(lambda x, y: y + x, arr, 'Y'))
'''
edcbaY
'''


lmax = lambda seq: functools.reduce(lambda x, y: x if x > y else y, seq)
lmin = lambda seq: functools.reduce(lambda x, y: x if x < y else y, seq)

lsum = lambda seq: functools.reduce(operator.add, seq)
lmul = lambda seq: functools.reduce(operator.mul, seq)

lany = lambda func, seq: functools.reduce(lambda x, y: x or func(y), seq, False)
lall = lambda func, seq: functools.reduce(lambda x, y: x and func(y), seq, True)

lmap = lambda func, seq: functools.reduce(lambda x, y: x + [func(y)], seq, [])
lfilter = lambda func, seq: functools.reduce(lambda x, y: x + [y] if func(y) else x, seq, [])


print(lany(lambda x: x % 2 == 0, [1, 3, 5, 7, 9, 2]))
print(lall(lambda x: x % 2 == 1, [1, 3, 5, 7, 9, 1]))
'''
True
True
'''