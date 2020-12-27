a = 5
b = 6
c = a * b

print(a)
print(b)
print(c)

name = input('Ваше имя: ')
age = int(input('Сколько вам лет: '))
flg = input('Вы отмечали день рождения в этом году? (да/нет) :')
bef = 2020 - age

if flg != 'да':
    bef = bef-1

print('Здравствуйте, '+name+'. Вы родились в '+str(bef)+' году')

