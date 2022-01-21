translate = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(words):
    if words.istitle():
        print(str(translate.get(words.lower())).title())
    else:
        print(str(translate.get(words)))


num_translate(input('Введите число на английском: '))
