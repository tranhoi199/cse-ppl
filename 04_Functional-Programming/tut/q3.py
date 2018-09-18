from functools import reduce



def revRecursive(a):
    return [] if len(a) == 0 else [a[-1]] + revRecursive(a[:-1])

def revHoF(lst):
    return list(reduce(lambda x,y: [y]+x, lst, []))

print(revRecursive([]))
print(revRecursive([1]))
print(revRecursive([1,2,3,4,5]))

print(revHoF([]))
print(revHoF([1]))
print(revHoF([1,2,3,4,5]))






def appendRec(a, b):
    return a if len(b) == 0 else appendRec(a+[b[0]], b[1:])

print(appendRec([], []))
print(appendRec([], [4,5,6]))
print(appendRec([1,2,3], []))
print(appendRec([1,2,3], [4,5,6]))


def appendHoF(a, b):
    return reduce(lambda x,y:x+[y], b, a)

print(appendHoF([], []))
print(appendHoF([], [4,5,6]))
print(appendHoF([1,2,3], []))
print(appendHoF([1,2,3], [4,5,6]))