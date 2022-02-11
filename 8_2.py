import re

parse = re.compile(r'[\w\.\:\+\/]+')

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for i in f:
        result = parse.findall(i)
    print(result)
    print((result[0], result[1] + ' ' + result[2], result[3], result[4], result[5], result[6], result[7]))


