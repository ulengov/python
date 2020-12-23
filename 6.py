a = float(input('Введите a: '))
b = float(input('Введите b: '))

n = 1

while True:
    if a>=b:
        break
    a = a * 1.1
    n = n + 1

print(n)


