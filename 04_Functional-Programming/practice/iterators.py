# An iterator is an object representing a stream of data;

arr = [1, 2, 3, 4, 5, 6, 7, 8]
it = iter(arr)

print(it.__next__())
print(it.__next__())
print(next(it))
print(next(it))

for i in it: 
    print(i)

'''
1
2
3
4
5
6
7
8
'''


it = iter(arr)
t = tuple(it)
print(t)
'''
(1, 2, 3, 4, 5, 6, 7, 8)
'''


L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')]
D = dict(iter(L))
print(D)
'''
{'Italy': 'Rome', 'France': 'Paris', 'US': 'Washington DC'}
'''