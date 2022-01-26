from sys import argv
from utils import currency_rates

if __name__ == '__main__':
    currency, *args = argv
    for i in args:
        print(currency_rates(i))
