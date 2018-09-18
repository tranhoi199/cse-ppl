from functools import reduce


def compose(*func):
    def h(*args):
        return reduce(lambda x,y: y() ,reversed(g),args)
    return h

def f(x, y, z):
    return x + y, y + z

def g(x, y):
    return x * 2, y *2

def h(x, y):
    return x + 1, y + 1, x + y

def k(x, y, z):
    return x * y * z

q = compose(k,h,g,f)

print(q(1,2,3))