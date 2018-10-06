from functools import reduce


def compose(*func):
    def h(*args):
        return reduce(lambda x,y: y(*x), reversed(func), args)
    return h

def f(x, y, z):
    return x + y, y + z

def g(x, y):
    return x * 2, y * 2

def h(x, y):
    return x + 1, y + 1, x + y

def k(x, y, z):
    return x * y * z

q = compose(k,h,g,f)

print(q(1,2,-1)) # 168

# k(h(g(f(1,2,-1))))
# f(1,2,-1) = 3, 1
# g(3,1) = 6, 2
# h(6,2) = 7, 3, 8
# k(7,3,8) = 7*3*8 = 168