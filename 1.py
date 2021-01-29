#Плохо понял задачу. Сделал только то. что понял

class MyDate:

    @classmethod
    def decode(cls,text):
        __dt = text.split('-')
        cls.day =int(__dt[0])
        cls.monf = int(__dt[1])
        cls.year = int(__dt[2])

    @staticmethod
    def valid(d,m):
        __tb = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return True if d <= __tb[m + 1] else False

while True:

    MyDate.decode(input('Введите дату в формате DD-MM-YYYY: '))

    print(f'{MyDate.day}/{MyDate.monf}/{MyDate.year}', MyDate.valid(MyDate.day,MyDate.monf))
