from bs4 import BeautifulSoup
import requests


def get_soup(url) -> BeautifulSoup:
    headers: dict = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, '
                                   'like Gecko) Chrome/131.0.0.0 Safari/537.36'}

    request = requests.get(url, headers=headers)
    html_content: bytes = request.content

    soup: BeautifulSoup = BeautifulSoup(html_content, 'html.parser')

    return soup


def get_headlines(soup: BeautifulSoup) -> list[str]:
    headlines: set = set()

    for h in soup.find_all(attrs={"data-testid": "card-headline"}):
        headline: str = h.get_text().lower()
        headlines.add(headline)

    return list(headlines)


def main():
    soup = get_soup('https://www.bbc.com/news/')
    headlines = get_headlines(soup=soup)
    for headline in headlines:
        print(headline)


if __name__ == '__main__':
    main()
