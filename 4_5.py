from sys import argv
from utils import currency_rates

word = argv[1]
print(currency_rates(word))

