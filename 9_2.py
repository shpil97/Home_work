class Road:
    def __init__(self, length=0, width=0):
        self._length = length
        self._width = width

    def calculation_formula(self, weight=25, thickness=1):
        print((self._length * self._width * weight * thickness) // 1000, 'т', sep='')


a = Road(20, 5000)
a.calculation_formula(25, 5)
