from abc import ABC, abstractmethod

class Odezda(ABC):

    @abstractmethod
    def rashod(self):
        pass

class Palto(Odezda):

    name = 'Пальто'

    def __init__(self, param):
        self.param = param

    @property
    def param(self):
        return self.__xyz

    @param.setter
    def param(self, param):
        if param < 40:
            self.__xyz = 40
        elif param > 62:
            self.__xyz = 62
        else:
            self.__xyz = param

    def rashod(self):
        return self.param/6.5 + 0.5

class Costum(Odezda):

    name = 'Костюм'

    def __init__(self, param):
        self.param = param

    @property
    def param(self):
        return self.__xyz

    @param.setter
    def param(self, param):
        if param < 1.50:
            self.__xyz = 1.50
        elif param > 2.00:
            self.__xyz = 2.00
        else:
            self.__xyz = param

    def rashod(self):
        return self.param*2 + 0.3

a = Palto(46)
b = Costum(1.75)

print(f'{a.name} размер {a.param} расход {round(a.rashod(),2)} метров')
print(f'{b.name} рост {b.param} расход {round(b.rashod(),2)} метров')
