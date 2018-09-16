import math
import functools


sub = lambda a, b: a-b
opposite = functools.partial(sub, 0) # default a = 0

print(sub(0, 5))
print(opposite(5))
'''
-5
-5
'''



distance = lambda x1, y1, x2, y2: math.sqrt((x1-x2)**2 + (y1-y2)**2)

distance_O = functools.partial(distance, 0, 0) # default x1, y1 = 0, 0

print(distance(0, 0, 4, 5))
print(distance_O(4, 5))
'''
6.4031242374328485
6.4031242374328485
'''