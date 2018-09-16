"""
Document:

enumerate(iter, start=0) counts off the elements in the iterable 
returning 2-tuples containing the count (from start) and each element.
"""


arr = ['Python', 'NodeJS', 'PHP']
print([i for i in enumerate(arr)])
'''
[(0, 'Python'), (1, 'NodeJS'), (2, 'PHP')]
'''



animals = [
    {'type': 'Dog', 'name': 'Lucy'},
    {'type': 'Cat', 'name': 'Buddy'},
    {'type': 'Rabbit', 'name': 'Jack'},
    {'type': 'Cat', 'name': 'Duke'},
    {'type': 'Rabbit', 'name': 'Sadie'},
    {'type': 'Dog', 'name': 'Bella'},
]

dogsName = [value['name'] for (idx, value) in enumerate(animals) if value['type'] == 'Dog']
print(dogsName)
'''
['Lucy', 'Bella']
'''