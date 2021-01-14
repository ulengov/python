from functools import reduce

def mul(a,b):
    return a * b

print(reduce(mul,[el for el in range(100,1001) if el % 2 == 0]))
