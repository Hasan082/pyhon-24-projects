from random import shuffle

from flask import Flask, render_template
app = Flask(__name__)

# Generate deck of 52 cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

card_images = {
    f"{rank} of {suit}": f"https://deckofcardsapi.com/static/img/{'0' if rank == '10' else rank}{suit[0]}.png"
    for suit in suits for rank in ranks
}


@app.route('/')
def index():
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    shuffle(deck)
    single_set = 13
    hands = [deck[i:i + single_set] for i in range(0, 52, single_set)]
    players = {

    }
    for i, hand in enumerate(hands):
        players_cards = []
        for card in hand:
            temp = {'image': card_images[card]}
            players_cards.append(temp)
        players[f"player {i + 1}"] = players_cards
    print(players)
    return render_template("index.html", players=players)


if __name__ == '__main__':
    app.run(debug=True)
