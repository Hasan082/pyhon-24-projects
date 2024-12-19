# https://gale.udemy.com/course/great-python-projects/learn/lecture/38187678#overview

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from download_chrome import download_chrome
import shutil


def is_chrome_installed() -> bool:
    """
    Checks if chrome is installed
    :return: True if chrome is installed, else False
    """
    if shutil.which("chrome") or shutil.which("google-chrome"):
        return True
    return False


def main(url_to_scrape: str) -> None:
    if is_chrome_installed():
        download_chrome()
        print("Chrome installed")
    else:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url_to_scrape)
        time.sleep(5)
        print(driver.title)
        driver.quit()


if __name__ == "__main__":
    url__user_input = input("Enter url to scrape: ")
    main(url__user_input)
