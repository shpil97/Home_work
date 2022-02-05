from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as file_r:
    if 1 < len(argv) < 4 and [i for i in argv[1:] if i.isdigit()]:
        if len(argv) == 3:
            start, finish = map(int, argv[1:])
            print(*(v for i, v in enumerate(file_r) if start - 1 <= i < finish), sep='')
        else:
            print(*(v for i, v in enumerate(file_r) if i >= int(argv[1]) - 1), sep='')
    else:
        print(file_r.read())