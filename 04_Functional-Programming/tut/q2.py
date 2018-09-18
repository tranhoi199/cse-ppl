from functools import reduce
from itertools import repeat

def powRecursive(x, n):
    return 1 if n == 0 else x * powRecursive(x, n-1)

print(powRecursive(1, 0))
print(powRecursive(1, 1))
print(powRecursive(1, 5))
print(powRecursive(5, 0))
print(powRecursive(5, 5))

def powHoF(x, n):
    return reduce(lambda a,b: a*b, list(repeat(x, n)), 1)

print(powHoF(1, 0))
print(powHoF(1, 1))
print(powHoF(1, 5))
print(powHoF(5, 0))
print(powHoF(5, 5))