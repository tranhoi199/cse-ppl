"""
Document:

filter(predicate, iter) returns an iterator over all the sequence elements 
that meet a certain condition, 
and is similarly duplicated by list comprehensions. 

A predicate is a function that returns the truth value of some condition; 
for use with filter(), the predicate must take a single value.
"""

def isEven(n):
    return n % 2 == 0

print(list(filter(isEven, range(10))))
print([x for x in range(10) if isEven(x)])
'''
[0, 2, 4, 6, 8]
[0, 2, 4, 6, 8]
'''


animals = [
    {'type': 'Dog', 'name': 'Lucy'},
    {'type': 'Cat', 'name': 'Buddy'},
    {'type': 'Rabbit', 'name': 'Jack'},
    {'type': 'Cat', 'name': 'Duke'},
    {'type': 'Rabbit', 'name': 'Sadie'},
    {'type': 'Dog', 'name': 'Bella'},
]


dogsName = list(filter(lambda animals: animals['type'] == 'Dog', animals))
dogsName = list(map(lambda animals: animals['name'], dogsName))
print(dogsName)
'''
['Lucy', 'Bella']
'''