"""
Document:

The any(iter) and all(iter) built-ins look at the truth values of an iterable’s contents.
any() returns True if any element in the iterable is a true value, and 
all() returns True if all of the elements are true values:
"""


animals = [
    {'type': 'Dog', 'name': 'Lucy'},
    {'type': 'Cat', 'name': 'Buddy'},
    {'type': 'Rabbit', 'name': 'Jack'},
    {'type': 'Cat', 'name': 'Duke'},
    {'type': 'Rabbit', 'name': 'Sadie'},
    {'type': 'Dog', 'name': 'Bella'},
]


allIsDog = all(map(lambda animal: animal['type'] == 'Dog', animals))
print(allIsDog)
'''
False
'''

filterDogs = [i for i in animals if i['type'] == 'Dog']
allIsDog = all(map(lambda animal: animal['type'] == 'Dog', filterDogs))
print(allIsDog)
'''
True
'''

anyIsDog = any(map(lambda animal: animal['type'] == 'Dog', animals))
print(anyIsDog)
'''
True
'''

anyIsHamster = any(map(lambda animal: animal['type'] == 'Hamster', animals))
print(anyIsHamster)
'''
False
'''