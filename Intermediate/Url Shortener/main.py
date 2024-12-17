from typing import Final
import requests

API_KEY: Final[str] = '4788e2e2e6e2aee5dae734315ddf13b50073c'
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'


def shorten_url(full_url: str) -> None:
    payload: dict = {
        'key': API_KEY,
        'short': full_url,
    }
    try:
        response = requests.post(BASE_URL, params=payload)
        data: dict = response.json()
    except Exception as e:
        print(f'Error: {e}')

    if url_data := data.get('url'):
        if url_data['status'] == 7:
            print(f"Shortened URL: {url_data['shortLink']}")
        else:
            print("Error shortening URL" + url_data['status'])


def main() -> None:
    full_url: str = input("Full URL: ")
    shorten_url(full_url)


if __name__ == '__main__':
    main()
