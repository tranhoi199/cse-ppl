from fibo import *
from myrandom import randomListInt


print([fiboNormal(i) for i in range(6)])

print([fiboOneline(i) for i in range(6)])

print(fiboArrayNormal(6))

print(fiboArrayOneline(6))


print(randomListInt(10, -50, 200))