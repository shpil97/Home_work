from itertools import zip_longest, islice

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

result = ((t, k) for t, k in zip_longest(tutors, klasses, fillvalue=None) if t)
print(type(result))
print(next(result))
print(next(result))
print(next(result))
print(*islice(result, 15))
print(*islice(result, 15))
