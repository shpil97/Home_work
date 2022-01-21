def thesaurus(names):
    people = {}
    for name in names:
        if name[0] in people.keys():
            people[name[0]].append(name)
        else:
            people[name[0]] = [name]

    for keys, val in people.items():
        print(keys, val)


nam = ['Мария', 'Павел', 'Игорь', 'Петр', 'Виталий', 'Виолетта', 'Ирина']
nam.sort()
thesaurus(nam)
