"""Код очень сырой, отправил его, чтобы закрыть ДЗ"""


class OrgTeh:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.price = 3000
        self.remains = 100
        self.order = []

    def realization(self):
        while True:
            product = ''
            try:
                request = int(input('укажите необходимый тип: \n1 - принтер \n2 - сканер \n3 - ксерокс\n'))
                if request == 'q':
                    break
                if request == 1:
                    product = 'printer'
                    self.remains = 20
                elif request == 2:
                    product = 'scanner'
                    self.remains = 15
                elif request == 3:
                    product = 'xerox'
                    self.remains = 25
                model = input(
                    f'вы выбрали {product} \nостаток склада: {self.remains}\nНазовите необходимого производителя\n')
            except ValueError:
                raise 'Некорректный ввод'
            try:
                col = int(input('кол-во техники'))
                if col < 10:
                    self.price = 4500
                    self.remains -= col
                elif 10 <= col <= 25:
                    self.price = 3500
                    self.remains -= col
                elif col > 25:
                    self.price = 3000
                    self.remains -= col
            except ValueError:
                return 'Некорректный ввод'
            try:
                self.remains -= col
                if self.remains < 0:
                    print('добавлено к заказу, ожидание уйдет 7-14 дней')
            except ValueError:
                return 'данный заказ можем осуществить через 7 дня'
            poz = {'модель': model, 'кол-во': col}
            self.order.append(poz)
            print(f'{self.order}, сумма заказа {self.price * col}р.')


class Warehouse:
    def __init__(self, model, price):
        super(OrgTeh).__init__()
        self.model = model
        self.price = price


class Printer(OrgTeh):
    def __init__(self, serial, name, year):
        super().__init__(name, year)
        self.series = serial


class Scaner(OrgTeh):
    def __init__(self, serial, name, year):
        super().__init__(name, year)
        self.series = serial


class Copier(OrgTeh):
    def __init__(self, serial, name, year):
        super().__init__(name, year)
        self.series = serial


unit_1 = Printer('hp', 2000, 12)
unit_1.realization()
