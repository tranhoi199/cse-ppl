"""
Document:
When you call a generator function, it doesn’t return a single value; 
instead it returns a generator object that supports the iterator protocol. 
On executing the yield expression, the generator outputs the value of i, 
similar to a return statement. 

The big difference between yield and a return statement is that 
on reaching a yield 
the generator’s state of execution is suspended and local variables are preserved. 
On the next call to the generator’s __next__() method, the function will resume executing.
"""

def yieldFunction():
    available = [3, 4, 1, 7, 9, 0, 2, 4, 3, 1, 5]
    for i in  available:
        if i % 2 == 0:
            yield i # as return, but only suspended the loop

# Get all return value as list
lst = list(yieldFunction())
print(lst)
'''
[4, 0, 2, 4]
'''

# Get iterator
it = yieldFunction()
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
'''
4
0
2
4
Traceback (most recent call last):
  File "./run.py", line 103, in <module>
    print(next(it))
StopIteration
'''