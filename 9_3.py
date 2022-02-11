class Worker:
    def __init__(self, name, surname, position, **kwargs):
        self.name = name
        self.surname = surname
        self.position = position
        if kwargs:
            self._income = kwargs


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname, self.position)

    def get_total_income(self):
        result = 0
        for key, val in self._income.items():
            result += val
        print(f'Заработная плата с учетом премии состовляет: {result}')


a = Position('Денис', 'Денисов', 'стажер', wage=500, bonus=500)
a.get_full_name()
a.get_total_income()
