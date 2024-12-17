from typing import Final
import requests

API_KEY: Final[str] = '4788e2e2e6e2aee5dae734315ddf13b50073c'
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'


def shorten_url(full_url: str) -> str:
    payload: dict = {'key': API_KEY, 'short': full_url}
    response = requests.post(BASE_URL, params=payload)
    data: dict = response.json()

    if url_data := data.get('url'):
        if url_data['status'] == 7:
            shortened_url:str = url_data['shortLink']
            print("Shortened url is: " + shortened_url)
        else:
            print("Something went wrong", url_data['status'])


def main():
    full_url = input('Full URL: ')
    shorten_url(full_url)


if __name__ == '__main__':
    main()



