class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'\33[7m Запуск отрисовки {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'\33[4m Запуск отрисовки {self.title}')



class Handle(Stationery):
    def draw(self):
        print(f'\33[7m Запуск отрисовки {self.title}')


a = Pen('Ручкой')
b = Pencil('Карандашом')
c = Handle('Маркером')
a.draw()
b.draw()
c.draw()
