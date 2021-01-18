f1 = open("1.txt", 'w')

while True:
    str = input('Введите строку: ')
    if str == '':
        break
    f1.write(str+'\n')

f1.close()
