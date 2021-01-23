class Stationery:

    def __init__(self, title = 'Stationery'):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Рисуем ручкой {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем карандашом {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Рисуем маркером {self.title}')

stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
