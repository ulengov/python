from itertools import count, cycle

def first(a,b):
    for el in count(a):
        if el > b:
            break
        else:
            print(el)

def second(a,b):
    i = 0
    for el in cycle(a):
        print(el)
        i += 1
        if i >= b:
            break


first(2,7)
print('---------------')
second([1, 2, 3, 4, 5, 6, 7],15)
