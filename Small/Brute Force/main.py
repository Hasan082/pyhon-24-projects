import itertools
import string
import time


def common_guess(word: str):
    with open("word.txt", "r") as f:
        words: list[str] = f.read().splitlines()

    for i, match in enumerate(words, start=1):
        if word == match:
            return f"Common Match: {match} (#{i})"


def bruit_force(word: str, length: int, digits: bool = False, symbols: bool = False) -> str | None:
    chars: str = string.ascii_lowercase

    if digits:
        chars += string.digits

    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess: str = "".join(guess)

        if guess == word:
            return f"{word} was cracked in {attempts} guesses."


def main():
    print("searching....")
    password: str = input("Password: ")

    start_time = time.perf_counter()

    if common_match := common_guess(password):  # := (Walrus Operator)
        print("Common Match:", common_match)
    else:
        if cracked := bruit_force(password, len(password), digits=True, symbols=False):
            print("Cracked Word:", cracked)
        else:
            print("Not Cracked Password")

    end_time = time.perf_counter()

    print(f"Time: {end_time - start_time:.2f}sec")


if __name__ == "__main__":
    main()
