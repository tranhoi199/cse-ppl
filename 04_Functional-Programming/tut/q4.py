def lessThanHoF(n, lst):
    return list(filter(lambda x: x < n, lst))

def lessThanRecursive(n, lst):
    return [] if len(lst) == 0 else ([lst[0]] if lst[0] < n else []) + lessThanRecursive(n, lst[1:])

print(lessThanRecursive(50, [1,2,3,60,12,14,25,50,6,100]))
print(lessThanHoF(50, [1,2,3,60,12,14,25,50,6,100]))
