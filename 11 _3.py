class DigitList(Exception):
    def __init__(self, num):
        self.num = num


my_list = []
while True:
    number_to_list = input('Введите числа! Чтобы программа завершилась, введите "stop"')
    try:
        if number_to_list == 'stop':
            break
        if number_to_list.isdigit():
            pass
        else:
            try:
                float(number_to_list)

            except ValueError:
                raise DigitList('Некорректный ввод')
        my_list.append(number_to_list)

    except DigitList as error:
        print(error)

print(my_list)
