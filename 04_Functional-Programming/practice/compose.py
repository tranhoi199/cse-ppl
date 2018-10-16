from functools import reduce


def compose(*g):
    def h(args):
        return reduce(lambda x,y: y(x), reversed(g), args)
    return h

def square(x):
   return x * x

def increase(x):
    return x + 1

def double(x):
   return x * 2

m = compose(square,increase,double)

print(m(5))

# square(increase(double(5))) = ((5*2)+1)^2
