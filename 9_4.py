from random import choice


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'автомобиль {self.name} {self.color} цвета, начал движение')

    def turn(self, direction):
        print(f'{direction}')

    def stop(self):
        print('Автомобиль совершил остановку')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
    def show_speed(self):
        if True:
            print('Ограничений нет')


direction_list = ['повернул налево', 'повернул направо', 'выполнил разворот']
town = TownCar('BMW', 'черного', 60, is_police=False)

town.go()
town.show_speed()
for i in range(5):
    town.turn(choice(direction_list))
town.stop()

work = WorkCar('Lada', 'белого', 88, is_police=False)
work.go()
work.show_speed()
for i in range(3):
    town.turn(choice(direction_list))
town.stop()

police = PoliceCar('skoda', 'белого', 90, is_police=True)
police.go()
police.show_speed()
for i in range(3):
    town.turn(choice(direction_list))
town.stop()
