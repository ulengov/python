class Sklad:

    def __init__(self):
        self.Spis = []

class Orgtex:

    def __init__(self,name, x, y, z, m):
        self.name = name #Название
        self.x = x  #длинна
        self.y = y  #шмрина
        self.z = z  #высота
        self.m = m  #масса

    def __str__(self):
        return self.name

class Printer(Orgtex):

   def __init__(self, name, lasr = False, x = 0, y = 0, z = 0, m = 0):
        super().__init__(name, x, y, z, m)
        self.laser = lasr   #Лазерный

class Skaner(Orgtex):

    def __init__(self, name, dpi = 600, x = 0, y = 0, z = 0, m = 0):
        super().__init__(name, x, y, z, m)
        self.dpi = dpi      #Разрешение

class Copir(Orgtex):

    def __init__(self, name, speed = 10, x = 0, y = 0, z = 0, m = 0):
        super().__init__(name, x, y, z, m)
        self.spiid = speed  #Скорость

p1 = Printer('Lasrjet 2000', True)

print(p1)
