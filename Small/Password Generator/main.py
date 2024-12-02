import string
import secrets
from random import random


def check_uppercase(word):
    for char in word:
        if char.isupper():
            return True
    return False


def check_symbol(word):
    for char in word:
        if char not in string.punctuation:
            return True
    return False


def generate_password(length: int, symbol: bool, uppercase: bool):
    combination = string.ascii_lowercase + string.digits

    if uppercase:
        combination += string.ascii_uppercase

    if symbol:
        combination += string.punctuation

    length_combination = len(combination)
    password = ""

    for i in range(length):
        password += combination[secrets.randbelow(length_combination)]

    return password


def main():
    length = int(input("Enter length of password: "))
    symbol = input("Symbol Required (True/False): ").strip().lower() == "true"
    uppercase = input("Character uppercase Required (True/False): ").strip().lower() == "true"
    password = generate_password(length, symbol, uppercase)
    print(password)


if __name__ == '__main__':
    main()
