sum = 0
flg = True

while flg:

    str = input('Введите строку чисел через проьбел либо q: ')

    if str[-1] == 'q':
        str = str[:-1]
        flg = False

    spis = str.split(' ')

    for i, a in enumerate(spis):
         if a !='':
            sum = sum + int(a)

    print(sum)



