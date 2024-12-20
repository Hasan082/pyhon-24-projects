import json
from typing import Final
import requests
import logging

BASE_URL: Final[str] = 'https://api.exchangeratesapi.io/v1/latest'
API_KEY: Final[str] = 'bddf948c4aedc26c997870530b0ebb38'


def get_rates(mock: bool = False) -> dict:
    if mock:
        try:
            with open('rates.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error("Couldn't find rates.json")
            return {}

    payload: dict = {'access_key': API_KEY}
    try:
        response = requests.get(BASE_URL, params=payload)
        data: dict = response.json()
        return data
    except requests.exceptions.RequestException:
        logging.error("Request failed")
        return {}
    except ValueError:
        logging.error("Invalid JSON")
        return {}


def get_currency(currency: str, rates: dict) -> float:
    currency: str = currency.upper()
    if currency in rates.keys():
        return rates.get(currency)
    else:
        raise ValueError(f'Currency {currency} not valid currency.')


def convert_rates(amount: float, base: str, vs: str, rates: dict) -> None:
    base_rate: float = get_currency(base, rates)
    vs_rate: float = get_currency(vs, rates)

    converted_amount: float = round((vs_rate / base_rate) * amount, 2)
    print(f'Converted amount: {converted_amount:,.4f} {vs}')


def main():
    data: dict = get_rates(mock=True)
    rates: dict = data.get('rates')

    if not rates:
        logging.error("Couldn't find rates")
        return

    try:
        amount_convert: float = float(input('How much amount you want to convert: '))
        which_currency: str = input('Which currency do you want to convert: ')
        what_currency: str = input('What currency do you want to convert: ')
        convert_rates(amount_convert, which_currency, what_currency, rates)
    except ValueError as e:
        logging.error("Please try with correct data: %s", e)


if __name__ == '__main__':
    main()
