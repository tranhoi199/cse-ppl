"""
Document:
"""

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibb = fibonacci()
for i in range(10):
    print(next(fibb), end=' ')

print()
fibb = fibonacci()
fibb10 = [next(fibb) for i in range(10)]
print(fibb10)

'''
0 1 1 2 3 5 8 13 21 34
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''


import time

# arr = ["first value", time.sleep(1), time.sleep(2)]
# print(arr[0]) 
# evaluation before print -> waste time but useless


arr = [lambda: "first value", lambda: time.sleep(1), lambda: time.sleep(2)]
print(arr[0]()) 
# elem is only function declare, but not evaluated, print take 0 seconds



foo = lambda b, x, y: x if b else y

# a = 0
# print(foo(a != 0, 5/a, a))
# Get division by zero
'''
Traceback (most recent call last):
  File "./run.py", line 42, in <module>
    print(foo(a != 0, 5/a, a))
ZeroDivisionError: division by zero
'''


foo = lambda b, x, y: x() if b else y()

a = 0
print(foo(a != 0, lambda: 5/a, lambda: a))
# This is OK, output is 0