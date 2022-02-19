from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0

    def __init__(self, volume):
        self.volume = volume

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Suit(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f'{res}'


class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.volume / 6.5) + 0.5


class Suit(Clothes):
    @property
    def consumption(self):
        return round((2 * self.volume + 0.3) / 100)


coat = Coat(40)
suit = Suit(178)

print(coat + suit)
