arr = [1, 2, 3, 4, 5, 6, 7, 8]

sqr = (i ** 2 for i in arr) # return iterator
print(list(sqr))
'''
[1, 4, 9, 16, 25, 36, 49, 64]
'''

cube = [i ** 3 for i in arr] # return list
print(cube)
'''
[1, 8, 27, 64, 125, 216, 343, 512]
'''


sqr_range_20_40 = [i ** 2 for i in arr if i ** 2 < 40 and i ** 2 > 20]
print(sqr_range_20_40)
'''
[25, 36]
'''


a1 = [1, 2, 3]
a2 = [5, 6, 7]
par = [(x, y) for x in a1 for y in a2]
print(par)
'''
(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)]
'''

import math

distance = lambda x1, y1, x2, y2: math.sqrt((x1-x2)**2 + (y1-y2)**2)

print(distance(4, 5, 1, 2))