# Сортировка пузырьком

import random

size = 10
array = [i for i in range(size)]
#random.shuffle(array)
print(array)

n = 1
while n < len(array):
    f = True
    for i in range(len(array) - n):
        if array[i] > array[i+1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            f = False
    if f:
        break
    n += 1
    print(array)

print(array)


