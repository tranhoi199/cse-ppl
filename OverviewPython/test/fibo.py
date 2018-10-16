from functools import reduce

def fiboNormal(n: int):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def fiboOneline(n: int):
    return reduce(lambda x,_: (x[1], x[0]+x[1]), range(n), (0,1))[0]


def fiboArrayNormal(n: int):
    f = [0, 1]
    for _ in range(n-2):
        f.append(f[-1] + f[-2])
    return f


def fiboArrayOneline(n: int):
    return reduce(lambda x,_: x+[x[-1]+x[-2]], range(n-2), [0,1])
