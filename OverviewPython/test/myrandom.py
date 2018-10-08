from random import randint

def randomListInt(size: int, start = 0, end = 10000):
    return [randint(start, end) for _ in range(size)]