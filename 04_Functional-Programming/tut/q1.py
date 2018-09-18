from functools import reduce

def lstSquareRecursive(n):
    return lstSquareRecursive(n-1) + [n**2] if n > 0 else []

print(lstSquareRecursive(0))
print(lstSquareRecursive(1))
print(lstSquareRecursive(5))
print(lstSquareRecursive(50))

def lstSquareHoF(n):
    return [i**2 for i in range(1,n+1)]

print(lstSquareHoF(0))
print(lstSquareHoF(1))
print(lstSquareHoF(5))
print(lstSquareHoF(50))