from requests import get, utils
from datetime import datetime


def currency_rates(currency_code):
    """The function displays the exchange rate for today"""
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    data_time = content.split('Date="')[1][:10].split('.')
    data_time = datetime(day=int(data_time[0]), month=int(data_time[1]), year=int(data_time[2])).date()

    for i in content.split('<CharCode>')[1:]:
        code = i[:3]
        result = i.split('<Value>')[1:][0].split('</Value>')[0].replace(',', '.')
        result = f'{float(result):.2f}'

        if currency_code.upper() == code:
            return f'{data_time}: курс {code}: {result}'


print(currency_rates('usd'))
print(currency_rates('eur'))
