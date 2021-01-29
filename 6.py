class Sklad:

    def __init__(self):
        self.spis = {}

    def add(self, obj):
        if obj.name in self.spis:
            self.spis[obj.name][0]+= 1
        else:
            self.spis[obj.name] = [1,obj]

class Orgtex:

    def __init__(self,name, t, x, y, z, m):
        self.name = name #Название
        self.type = t   #тип 1,2,3
        self.x = x  #длинна
        self.y = y  #шмрина
        self.z = z  #высота
        self.m = m  #масса

    def __str__(self):
        return self.name

class Printer(Orgtex):

   def __init__(self, name, lasr = False, x = 0, y = 0, z = 0, m = 0):
        super().__init__(name, 1, x, y, z, m)
        self.laser = lasr   #Лазерный

class Skaner(Orgtex):

    def __init__(self, name, dpi = 600, x = 0, y = 0, z = 0, m = 0):
        super().__init__(name, 2, x, y, z, m)
        self.dpi = dpi      #Разрешение

class Xerox(Orgtex):

    def __init__(self, name, speed = 10, x = 0, y = 0, z = 0, m = 0):
        super().__init__(name, 3, x, y, z, m)
        self.spiid = speed  #Скорость

def digit(str):
    try:
        return int(str)
    except ValueError:
        return 0

sklad = Sklad()

print('Завершение ввода - пустая строка в названии')

while True:

    s = input('Название: ')
    if s == '':
        break

    t = digit(input('1 - Принтер 2 - Сканер 3 - Ксерох: '))
    x = digit(input('Длинна: '))
    y = digit(input('Ширина: '))
    z = digit(input('Высота: '))
    m = digit(input('Масса: '))
    if t == 1:
        p = digit(input('Лазерный? 0/1: '))
        obj = Printer(s, bool(p), x, y, z, m)
    elif t == 2:
        p = digit(input('Разрешение dpi: '))
        obj = Skaner(s, p, x, y, z, m)
    elif t == 3:
        p = digit(input('Скорость: '))
        obj = Xerox(s, p, x, y, z, m)
    n = digit(input('Количество: '))

    for i in range(n):
        sklad.add(obj)

for key in sklad.spis:
    print(sklad.spis[key][0],sklad.spis[key][1].name)
