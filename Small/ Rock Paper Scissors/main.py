import random
import sys


class RPSGame:
    def __init__(self):
        print("Welcome to Rock Paper Scissor!")

        self.moves: dict = {"rock": '🪨', "paper": '📄', 'scissors': '✂️'}
        self.valid_moves: list = list(self.moves.keys())

    def play_game(self):
        user_move: str = input("Which one you choose: Rock, paper, scissors: ->  ").lower()

        if user_move == 'exit':
            print("Thank you for playing!")
            sys.exit()

        if user_move not in self.valid_moves:
            print("Invalid move!")
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_move(user_move, ai_move)

    def display_moves(self, user_move: str, ai_move: str):
        print("----------")
        print(f"You chose {self.moves[user_move]}")
        print(f"AI chose {self.moves[ai_move]}")
        print("----------")

    def check_move(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print("It's a tie!")
        elif user_move == 'rock' and ai_move == 'scissors':
            print("You win!")
        elif user_move == 'scissors' and ai_move == 'paper':
            print("You win!")
        elif user_move == 'paper' and ai_move == 'rock':
            print("You win!")
        else:
            print("AI Wins!")


if __name__ == '__main__':
    rps = RPSGame()
    while True:
        rps.play_game()
