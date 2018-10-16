# [[1,2,3], [4,5,6], [7], [8,9]] -> [1,2,3,4,5,6,7,8,9]

arr = [[1,2,3], [4,5,6], [7], [8,9]]

#### Method 1: Use sum()
print(sum(iterable = arr, start = []))
# or simpler
print(sum(arr, []))


#### Method 2: Use reduce()
from functools import reduce
print(reduce(lambda lst, ele: lst + ele, arr, [])) # such as sum()


#### Method 3: Use [for]
print([i for sublist in arr for i in sublist])