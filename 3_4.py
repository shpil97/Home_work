def thesaurus(names):
    people = {}
    for name in names:
        people.setdefault(name.split()[-1][0], {}).setdefault(name[0], []).append(name)

    for key, val in people.items():
        print(key, val)

    # list_keys = list(people.keys())
    # list_keys.sort()
    # for i in list_keys:
    #     print(i, ':', people[i])   # """сортировка по ключам"""


peoples = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]
peoples.sort()
thesaurus(peoples)
