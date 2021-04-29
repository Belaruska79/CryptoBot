import json
import requests

from config import exchanger

class ConverterException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(values):
    if len(values) != 3:
        raise ConverterException(f'Неверное количество знаков')
    quote, base, amount = values


    if quote == base:
        raise ConverterException(f'Невозможно перевести одинаковые балюты {base}')

    try:
        quote_ticker = exchanger[quote]
    except KeyError:
        raise APIException ('Не удалось обработать валюту {quote}')

    try:
        amount = float(amount)
    except ValueError:
        raise ConverterException(f'Не удалось обработать количество {amount}')

    r = requests.get(f'https://api.exchangeratesapi.io/latest?base={quote_formatted}&symbols={base_formatted}')

    result = float(json.loads(r.content)['rates'][base_formatted]) * amount
    total = round(float(amont) * float(json.loads(r.content)['rates'][exchanger[base]]), 2)

    return round(result, 3)
