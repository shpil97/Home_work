class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number > 0:
            self.number -= other.number
        else:
            print('отрицательное число')
        return Cell(self.number)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __floordiv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, smile):
        return str(self.number) + '\n' + ''.join(
            [f'{chr(129499)}\n' if (i + 1) % smile == 0 else chr(129499) for i in range(self.number)])


c1 = Cell(10)
c2 = Cell(2)

print((c1 * c2).make_order(5))
print((c1 + c2).make_order(5))
print((c1 // c2).make_order(5))
print((c1 - c2).make_order(5))