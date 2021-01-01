def func(a,b):
    if b != 0:
        return a / b
    else:
        return None

a = float(input('Ведите делимое: '))
b = float(input('Ведите делитель: '))

print(func(a,b))
