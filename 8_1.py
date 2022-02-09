import re


def email_pars(email):
    mail = re.compile(r'(^[\w\-]*)\@([\w]+\.[a-z]*$)')
    if mail.match(email) is None:
        raise ValueError(f'wrong email: {email}')
    else:
        result = mail.findall(email)
        return {'username': result[0][0], 'domain': result[0][1]}


print(email_pars('someone@geekbrains.ru'))
print(email_pars('shpilev64@gmail.com'))
print(email_pars('asics1313@yandex.ru'))
