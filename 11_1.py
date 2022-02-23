class Date:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def int_date(cls, str_date):
        date, month, year = map(int, str_date.split('.'))
        if cls.valid_date(date, month):
            print(date, month, year)
        else:
            print('Неверная дата')

    @staticmethod
    def valid_date(date, month):
        if 0 < date < 32 and 0 < month < 12:
            return True


Date.int_date('18.02.2022')
Date.int_date('18.00.2022')
