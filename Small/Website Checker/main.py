import csv
import sys

import requests
from fake_useragent import UserAgent
from http import HTTPStatus


def get_websites(csv_path: str) -> list[str]:
    websites: list[str] = []
    with open(csv_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if 'https://' not in row[1]:
                websites.append(f"https://{row[1]}")
            else:
                websites.append(row[1])

    return websites


def get_user_agents() -> str:
    ua = UserAgent()
    return ua.chrome


def get_status_description(status_code: int) -> str:
    for value in HTTPStatus:
        if value == status_code:
            description: str = f'({value} {value.name}).{value.description}'
            return description

    return '(???) Unknown Status Code........'


def check_website(websites: list[str], user_agent) -> None:
    try:
        code: int = requests.get(websites, headers={'User-Agent': user_agent}).status_code
        print(websites, get_status_description(code))
    except requests.exceptions.RequestException:
        print(f'{websites} not found')


def main():
    sites = get_websites('websites.csv')
    user_agents = get_user_agents()

    for site in sites:
        check_website(site, user_agents)


if __name__ == '__main__':
    main()
