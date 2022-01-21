from random import choice, shuffle

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num=1, flag=True):
    """The function of forming jokes
    Returns num jokes from three random words,
    one from each list."""
    result = []
    if flag is True:
        for i in range(num):
            noun, adverb, adjective = choice(nouns), choice(adverbs), choice(adjectives)
            result.append(f'{noun} {adverb} {adjective}')
    if flag is False:
        for i in range(num):
            noun, adverb, adjective = choice(nouns), choice(adverbs), choice(adjectives)
            result.append(f'{noun} {adverb} {adjective}')
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)

    return result


print(get_jokes(int(input('введите количесво шуток: ')), flag=True))
