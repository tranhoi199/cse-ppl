"""
Document:
"""


animals = [
    {'type': 'Dog', 'name': 'Lucy'},
    {'type': 'Cat', 'name': 'Buddy'},
    {'type': 'Rabbit', 'name': 'Jack'},
    {'type': 'Cat', 'name': 'Duke'},
    {'type': 'Rabbit', 'name': 'Sadie'},
    {'type': 'Dog', 'name': 'Bella'},
]

ascSortedByType = sorted(animals, key=lambda i: i['type'])
print(ascSortedByType)
'''
[
    {'type': 'Cat', 'name': 'Buddy'}, 
    {'type': 'Cat', 'name': 'Duke'}, 
    {'type': 'Dog', 'name': 'Lucy'}, 
    {'type': 'Dog', 'name': 'Bella'}, 
    {'type': 'Rabbit', 'name': 'Jack'}, 
    {'type': 'Rabbit', 'name': 'Sadie'}
]
'''

descSortedByType = sorted(animals, key=lambda i: i['type'], reverse=True)
print(descSortedByType)
'''
[
    {'type': 'Rabbit', 'name': 'Jack'}, 
    {'type': 'Rabbit', 'name': 'Sadie'}, 
    {'type': 'Dog', 'name': 'Lucy'}, 
    {'type': 'Dog', 'name': 'Bella'}, 
    {'type': 'Cat', 'name': 'Buddy'}, 
    {'type': 'Cat', 'name': 'Duke'}
]
'''