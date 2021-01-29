class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

spis =[]

while True:

    try:
        a = input('Введите число или "stop": ')

        if a == 'stop':
            break

        b = a if a[0] != '-' else a[1:]

        if not b.isdigit():
            raise MyError('Это не число!')

        spis.append(int(a))

    except MyError as err:
        print(err)

print(spis)