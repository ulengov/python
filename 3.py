class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

work = Worker("Иван", "Петров", "Директор", 200, 20)

dol1 = Position("Иван", "Петров", "Директор", 200, 20)
dol2 = Position("Сергей", "Смирнов", "Бухгалтер", 100, 15)
dol3 = Position("Петр", "Сафронов", "Водитель", 50, 10)

print(dol1.get_full_name(), dol1.get_total_income())
print(dol2.get_full_name(), dol2.get_total_income())
print(dol3.get_full_name(), dol3.get_total_income())
