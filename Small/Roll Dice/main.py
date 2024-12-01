from random import randint
from collections import Counter

print("Welcome to Dice Roll game! Input a number between 1 and 100. If you want to exit write \'exit\'")


def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError()
    rolls = [randint(1, 6) for _ in range(amount)]
    counter_dict = Counter(rolls)
    max_num = max(counter_dict, key=counter_dict.get)
    counts = counter_dict[max_num]
    print(f"{max_num} shows {counts} maximum times. So {max_num} is win!")
    return rolls


def main():
    while True:
        try:
            user_input = input('Enter a number: ')
            if user_input.lower() == 'exit':
                print("Thanks for playing")
                break
            print(*roll_dice(int(user_input)), sep=", ")
        except ValueError as e:
            print("Please enter a valid number")


if __name__ == '__main__':
    main()
