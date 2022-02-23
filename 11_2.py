class Error(Exception):
    def __init__(self, num):
        self.num = num


a = input()
b = input()
try:
    a = int(a)
    b = int(b)
    if a == 0 or b == 0:
        raise Error('На 0 делить нельзя')
    elif a // b > 0:
        print(a // b)

except ValueError:
    print('Введите число')

except Error as err:
    print(err)


