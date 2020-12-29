str = input('Введите строку с пробелами :')

spis = str.split(' ')

for i,a in enumerate(spis):
    print(i,a[:10])