import requests
from dataclasses import dataclass
from typing import Final
import logging

BASE_URL: Final[str] = 'https://api.coingecko.com/api/v3/coins/markets'


@dataclass
class Coin:
    name: str
    symbol: str
    current_price: float
    high_24h: float
    low_24h: float
    price_change_24h: float
    price_change_percent_24h: float

    def __str__(self):
        return f'{self.name} ({self.symbol}): ${self.current_price:,.2f}'


def get_coins() -> list[Coin]:
    jsonData: dict = {}
    try:
        payload: dict = {'vs_currency': 'usd', 'order': 'market_cap_desc'}
        data = requests.get(BASE_URL, params=payload)
        jsonData: dict = data.json()
    except Exception as e:
        logging.error("API ERROR" + str(e))

    coin_list: list[Coin] = []
    for item in jsonData:
        current_coin: Coin = Coin(item.get('name'),
                                  item.get('symbol'),
                                  item.get('current_price'),
                                  item.get('high_24h'),
                                  item.get('low_24h'),
                                  item.get('price_change_24h'),
                                  item.get('price_change_percent_24h'))

        coin_list.append(current_coin)

    return coin_list


if __name__ == '__main__':
    coins: list[Coin] = get_coins()
    for coin in coins:
        print(coin)

