for i in range(1, 101):
    if 10 < i < 15:
        print(i, 'Процентов')
    elif i % 10 == 1:
        print(i, 'процент')
    elif i % 10 > 1 and i % 10 < 5:
        print(i, 'процента')
    else:
        print(i, 'процентов')
