class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        return Matrix(map(lambda r_1, r_2: map(lambda x, y: x + y, r_1, r_2), self.matrix, other.matrix))

    def __str__(self):
        return ''.join(f'{i}\n' for i in zip(*self.matrix)).replace('(', '').replace(')', '').replace(',', '')


m1 = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
print(m1)
m2 = Matrix([[7, 8, 9], [9, 10, 11], [11, 12, 13]])
print(m2)
print(m1 + m2)

