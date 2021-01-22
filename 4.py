class Car:
    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        self.speed = 0

    def go(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def show_speed(self):
        return self.speed

class TownCar(Car):
    def show_speed(self):
        return self.speed if self.speed<60 else 'Превышение'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        return self.speed if self.speed<40 else 'Превышение'

class PoliceCaar(Car):
    pass

car1= TownCar('Blue', 'Camry', False)
car2= SportCar('Red', 'Lamborjini', False)
car3= WorkCar('Dark', 'Haice', False)
car4= PoliceCaar('White', 'Vista', True)

car1.go(100)
car2.go(110)
car3.go(120)
car4.go(130)

print(car1.show_speed())
print(car2.show_speed())
print(car3.show_speed())
print(car4.show_speed())

car1.stop()
car2.stop()
car3.stop()
car4.stop()
