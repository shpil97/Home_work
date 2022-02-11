from time import sleep


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        while True:
            for k, v in self.__color.items():
                print(k)
                sleep(v)


result = {f'\033[31m red': 7, '\033[33m yellow': 2, '\033[32m green': 2}

a = TrafficLight(result)
a.running()

