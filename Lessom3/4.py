def my_func1(x,y):
    return x ** y

def my_func2(x,y):
    n = abs(y)
    k = 1
    while n>0:
        k = k * x
        n -=1
    if y < 0:
        k = 1/k
    return k

x = float(input('Введите действительное положительное Х>0: '))
y = int(input('Введите целое отрицательное y: '))

print(my_func1(x,y))
print(my_func2(x,y))
