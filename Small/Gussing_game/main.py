from random import randint

lower_num, higher_num = 1, 10

random_num: int = randint(lower_num, higher_num)
print(random_num)
print(f"Guess The number between {lower_num} and {higher_num}")

while True:
    try:
        user_guess: int = int(input("Guess The number: "))
        if user_guess < 1 or user_guess > higher_num:
            raise ValueError
    except ValueError as e:
        print("Please enter a valid number between 1 and 10")
        continue

    if user_guess > random_num:
        print(f"You guessed Higher number")
    elif user_guess < random_num:
        print(f"You guessed Lower number")
    else:
        print(f"Congratulations! You guessed it")
        break
