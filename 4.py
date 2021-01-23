class Car:
    def __init__(self, color, name, is_police = False):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = 0

    def go(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def show_speed(self):
        return self.speed

class TownCar(Car):
    def show_speed(self):
        return self.speed if self.speed<60 else f'{self.speed} Превышение!'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        return self.speed if self.speed<40 else f'{self.speed} Превышение!'

class PoliceCar(Car):
    def __init__(self, color, name, is_police = True):
        super().__init__(color, name, is_police)


car1= TownCar('Blue', 'Camry')
car2= SportCar('Red', 'Lamborjini')
car3= WorkCar('Dark', 'Haice')
car4= PoliceCar('White', 'Vista')

car1.go(100)
car2.go(110)
car3.go(120)
car4.go(130)

print(f'Автомобиль: {car1.name} Цвет: {car1.color} Полицейский: {car1.is_police} Скорость: {car1.show_speed()}')
print(f'Автомобиль: {car2.name} Цвет: {car2.color} Полицейский: {car2.is_police} Скорость: {car2.show_speed()}')
print(f'Автомобиль: {car3.name} Цвет: {car3.color} Полицейский: {car3.is_police} Скорость: {car3.show_speed()}')
print(f'Автомобиль: {car4.name} Цвет: {car4.color} Полицейский: {car4.is_police} Скорость: {car4.show_speed()}')

car1.stop()
car2.stop()
car3.stop()
car4.stop()
