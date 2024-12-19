import re
import csv
from typing import Final
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

EMAIL_REGEX: Final[str] = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""


def save_csv(list_of_emails: set, filename: str = 'emails.csv') -> None:
    if not list_of_emails:
        print('No emails found.')
        return None

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Email'])
        for email in list_of_emails:
            writer.writerow([email])


class Browser:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-gpu")

        self.service = Service()
        self.browser = webdriver.Chrome(service=self.service, options=self.chrome_options)

    def scarp_email(self, url: str) -> str:
        print(f"Scarping email: {url}")
        self.browser.get(url)
        page_source = self.browser.page_source

        list_of_emails: set = set()
        for re_math in re.finditer(EMAIL_REGEX, page_source):
            list_of_emails.add(re_math.group())

        return list_of_emails

    def close_browser(self):
        print("Closing browser")
        self.browser.close()


def main():
    browser = Browser()

    emails: set = browser.scarp_email("https://www.randomlists.com/email-addresses?qty=150")
    print(f"Emails: {list(emails)}\n{len(list(emails))}")
    # Save the email in CSV
    save_csv(emails)


if __name__ == "__main__":
    main()
