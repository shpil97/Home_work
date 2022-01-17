massage = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for num, word in enumerate(massage):
    sign = '"'
    sign_1 = None
    if word.isdigit():
        massage[num] = f'{sign}{int(word):02}{sign}'
    if word.count('+'):
        word = word.replace('+', '')
        sign_1 = '+'
        massage[num] = f'{sign}{sign_1}{int(word):02}{sign}'
    elif word.count('-'):
        word = word.replace('-', '')
        sign_1 = '-'
        massage[num] = f'{sign}{sign_1}{int(word):02}{sign}'

print(' '.join(massage))
