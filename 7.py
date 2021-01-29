class Compl:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b > 0:
            return f'{self.a}+{self.b}i'
        else:
            return f'{self.a}{self.b}i'

    def __add__(self, other):
        res = Compl(self.a,self.b)
        res.a += other.a
        res.b += other.b
        return res

    def __mul__(self, other):
        res = Compl(0,0)
        res.a = self.a * other.a - self.b * other.b
        res.b = self.a * other.b + self.b * other.a
        return res

c1 = Compl(1,-1)
c2 = Compl(-2,2)

print('c1 =',c1)
print('c1 =',c2)
print('c1 + c2 =', c1 + c2)
print('c1 * c2 =', c1 * c2)
