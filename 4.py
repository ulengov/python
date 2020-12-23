num = int(input('Введите целое проложителное число: '))

max = 0

while num // 10 >0:
    if num % 10 > max:
        max = num % 10
    num = num //10

print(max)
