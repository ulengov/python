class Cell():

    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count >= other.count:
            return Cell(self.count - other.count)
        else:
            raise TypeError

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, line):
        return '\n'.join((['*' * line for _ in range(self.count // line)]))  + '\n'  + '*' * (self.count % line)  + '\n'

c1 = Cell(6)
c2 = Cell(4)
c3 = c1 + c2
c4 = c1 - c2
c5 = c1 * c2
c6 = c1 / c2

print(c3.count, c4.count, c5.count, c6.count)
print(c3.make_order(5))
print(c4.make_order(5))
print(c5.make_order(5))
print(c6.make_order(5))
