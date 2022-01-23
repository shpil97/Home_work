from requests import get, utils
from datetime import date


def currency_rates(currency_code):
    """The function displays the exchange rate for toda"""
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    date_time = content.split('Date="')[1][:10].split('.')
    date_time = date(day=int(date_time[0]), month=int(date_time[1]), year=int(date_time[2]))

    for i in content.split('<CharCode>')[1:]:
        code = i[:3]
        result = (i.split('<Value>')[1:][0].split('</Value>')[0])
        result = result.replace(',', '.')
        result = float(f'{float(result):.2f}')

        if currency_code.upper() == code:
            return f'{date_time}: курс {code} {result}'


if __name__ == '__mane__':
    print('import')
