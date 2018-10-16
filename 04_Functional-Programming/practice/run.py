# [[1,2,3], [4,5,6], [7], [8,9]] -> [1,2,3,4,5,6,7,8,9]

arr = [[1,2,3], [4,5,6], [7], [8,9]]

#### Method 1: Use sum()
print(sum(arr, []))
# interator: arr, start: []
# such as reduce()


#### Method 2: Use reduce()
from functools import reduce
print(reduce(lambda lst, ele: lst + ele, arr, [])) # such as sum()


#### Method 3: Use [for]
print([i for sublist in arr for i in sublist])

# ???, please:
print([(i,j) for i in range(4) for j in range(i)])
# [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2)]
print([(i,j,k) for i in range(5) for j in range(i) for k in range(j)])
# [(2, 1, 0), (3, 1, 0), (3, 2, 0), (3, 2, 1), (4, 1, 0), (4, 2, 0), (4, 2, 1), (4, 3, 0), (4, 3, 1), (4, 3, 2)]