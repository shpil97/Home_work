from itertools import zip_longest
from json import dump


def hob_user(text):
    with open(text, 'r', encoding='utf-8') as f:
        for i in f:
            yield i.rstrip().replace(',', ' ')


result = {}
with open('u_h.json', 'w', encoding='utf-8') as file_2:
    for key, val in zip_longest(hob_user('users.csv'), hob_user('hobby.csv')):
        result.setdefault(key, val)
        if key is None:
            exit(1)
    dump(result, file_2, ensure_ascii=False, indent=4)

print(result)


