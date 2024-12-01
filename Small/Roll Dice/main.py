from random import randint


def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError()
    rolls = [randint(1, 6) for _ in range(amount)]

    return rolls


def main():
    while True:
        try:
            user_input = input('Enter a number: ')
            if user_input.lower() == 'exit':
                print("Thanks for playing")
                break
            print(roll_dice(int(user_input)))
        except ValueError as e:
            print("Please enter a valid number")


main()
