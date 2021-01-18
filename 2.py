f1 = open("2.txt", 'r')

cnt = 0

for line in f1:
    cnt +=1
    print(f'Строка {cnt} слов: {len(line.split(" "))}')

print(f'Всего строк: {cnt}')

f1 .close()
