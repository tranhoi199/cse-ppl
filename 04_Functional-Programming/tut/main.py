def lookup(pattern, lst, cmp):
    arr = list(filter(lambda x: cmp(x) == pattern, lst))
    return None if arr == [] else arr[0]

res = lookup("hello", 
    # [('hello', 200), ('a', 50), ('he', 0), ('olleh', 500), ('olleh', 200), ('olleh', 100)],
    [('hello', 200), ('a', 50), ('he', 0)],
    lambda x: x[0][::-1]) # reversed

print(res)