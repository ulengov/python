class Matrix:

    def __init__(self, mat):
        self.x = len(mat[0])
        self.y = len(mat)
        self.mat = mat

    def __str__(self):
        res =  ''
        for y in range(0, len(self.mat)):
            res = res + str(self.mat[y]) + '\n'
        return res

    def __add__(self, other):
        if (self.x == other.x) and (self.y == other.y):
            res = Matrix(self.mat)
            for y in range(0, len(res.mat)):
                for x in range(0, len(res.mat[y])):
                    res.mat[y][x] += other.mat[y][x]
            return res
        else:
            raise TypeError

mat1 = Matrix([[1,2,3],[4,5,6]])
mat2 = Matrix([[-1,-2,-3],[-4,-5,-6]])

print(mat1)
print(mat2)
print(mat1 + mat2)
