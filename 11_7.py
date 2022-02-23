class ComplexNumbers:
    def __init__(self, num, num_2):
        self.num = num
        self.num_2 = num_2

    def __str__(self):
        return f'({self.num}+{self.num_2}j)'

    def __add__(self, other):
        return ComplexNumbers(self.num + other.num, self.num_2 + other.num_2)

    def __mul__(self, other):
        return ComplexNumbers(self.num * other.num - self.num_2 * other.num_2,
                              self.num * other.num_2 + self.num_2 * other.num)


a = ComplexNumbers(5, 6)
b = ComplexNumbers(3, 1)

print(a + b)
print(a * b)
