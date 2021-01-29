class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:

    try:
        a = int(input('Введите число: '))

        if a == 0:
            raise MyError('Деление на 0!')

        print(f'1/{a} = {1/a}')

    except ValueError:
        print("Вы ввели не число")

    except MyError as err:
        print(err)
