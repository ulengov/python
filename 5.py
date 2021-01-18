from functools import reduce
from random import randint

def sum(a,b):
    return int(a) + int(b)

f1 = open("5.txt", 'w')
f1.write(' '.join([str(randint(1,99)) for _ in range(200)]))
f1.close()

f2 = open("5.txt", 'r')
print(reduce(sum,f2.read().split(' ')))
f2.close()
