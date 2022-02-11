import re


def email_pars(email):
    mail = re.compile(r'(^[\w\-]*)\@([\w]+\.[a-z]*$)')
    if mail.match(email) is None:
        raise ValueError(f'wrong email: {email}')
    else:
        result = mail.findall(email)
        return {'username': result[0][0], 'domain': result[0][1]}




for i in ['someone@geekbrains.ru','shpilev64@gmail.com','asics1313@yandex.ru']:
    try:
        print(email_pars(i))
    except ValueError as err:
        print(err)
