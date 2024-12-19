from crypto_data import Coin, get_coins
import time
import logging


def alerter(symbol: str, lower_limit: float, upper_limit: float, coin_list: list[Coin]) -> None:
    for coin in coin_list:
        if coin.symbol == symbol:

            if coin.current_price > upper_limit:
                print(f"{coin} | High Price | TRIGGER ALERT!!")
            elif coin.current_price < lower_limit:
                print(f"{coin} | Low Price | TRIGGER ALERT!!")
            else:
                print(f"{coin} | Within normal range.")

            if coin.current_price > coin.high_24h:
                print(
                    f"{coin} | Today's Highest Alert!! Current Price: ${coin.current_price:,.2f} | Highest 24h: ${coin.high_24h:,.2f}")
            elif coin.current_price < coin.low_24h:
                print(
                    f"{coin} | Today's Lowest Alert!! Current Price: ${coin.current_price:,.2f} | Lowest 24h: ${coin.low_24h:,.2f}")


if __name__ == '__main__':
    try:
        coins: list[Coin] = get_coins()

        while True:
            alerter('btc', lower_limit=90000, upper_limit=97100, coin_list=coins)
            alerter('eth', lower_limit=1800, upper_limit=3400, coin_list=coins)
            time.sleep(30)

    except Exception as e:
        logging.error(f"Error occurred: {e}")
