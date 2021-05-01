# class Person

from collections import namedtuple
from operator import attrgetter

Person = namedtuple('Person', 'name, age')

p_1 = Person('Вова', 25)
p_2 = Person('Саша', 30)
p_3 = Person('Лера', 23)

people = [p_1, p_2, p_3]

print(people)

result = sorted(people, key = attrgetter('age'))

print(result)

