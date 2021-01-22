class Stationery:
    title = 'Канцтовары'
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    title = 'Ручка'
    def draw(self):
        print('Рисуем ручкой')

class Pencil(Stationery):
    title = 'Карандаш'
    def draw(self):
        print('Рисуем карандашом')

class Handle(Stationery):
    title = 'Маркер'
    def draw(self):
        print('Рисуем маркером')

stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
