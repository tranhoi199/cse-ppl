"""
Document:

map(func, iterA, iterB, ...) returns an iterator over the sequence
"""

def upper(s):
    return str(s).upper()

lst = ['hello', ',', 'I', 'am', 'Python']


print(list(map(upper, lst)))
print([upper(s) for s in lst])
print([str(s).upper() for s in lst])
'''
['HELLO', ',', 'I', 'AM', 'PYTHON']
['HELLO', ',', 'I', 'AM', 'PYTHON']
['HELLO', ',', 'I', 'AM', 'PYTHON']
'''


animals = [
    {'type': 'Dog', 'name': 'Lucy'},
    {'type': 'Cat', 'name': 'Buddy'},
    {'type': 'Rabbit', 'name': 'Jack'},
    {'type': 'Cat', 'name': 'Duke'},
    {'type': 'Rabbit', 'name': 'Sadie'},
    {'type': 'Dog', 'name': 'Bella'},
]

dogsName = list(map(lambda animal: animal['name'] if animal['type'] == 'Dog' else None, animals))
dogsName = list(filter(lambda name: name != None, dogsName))
print(dogsName)
'''
['Lucy', 'Bella']
'''