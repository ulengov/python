#Сортировка Хоара (быстрая) Нужен опорный элемент

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)

def quick_sort(array):

    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    s_ar, m_ar, l_ar = [], [], []

    for item in array:

        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        else:
            raise Ellipsis('Непредвиденное')

    return quick_sort(s_ar) + m_ar + quick_sort(l_ar)

def quick_nmem(array, fst, lst):

    if fst >= lst:
        return

    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst

    while i <=j:

        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j -1

    quick_nmem(array, fst, j)
    quick_nmem(array, i, lst)

newar = quick_sort(array)
quick_nmem(array, 0, len(array) - 1)

print(newar)
print(array)
