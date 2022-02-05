from collections import Counter

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    dict_1 = Counter()
    for i in f:
        dict_1[i.split()[0]] += 1

    url, count = dict_1.most_common(1)[0][0], dict_1.most_common(1)[0][1]
    print(f'Пользователь "{url}" отправил {count} запросов')
