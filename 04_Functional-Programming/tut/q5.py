def lookup(pattern, lst, cmp):
    return list(filter(lambda x: cmp(x) == pattern, lst))

res = lookup("hello", 
    [('olleh', 100), ('hello', 200), ('a', 50), ('he', 0), ('olleh', 500), ('olleh', 200)],
    lambda x: x[0][::-1]) # reversed

print(res)