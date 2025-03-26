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
    hands = [deck[i:i + 13] for i in range(0, 52, 13)]
    players = {
        f"player {i + 1}": [{'image': card_images[card]} for card in hand]
        for i, hand in enumerate(hands)
    }
    return render_template("index.html", players=players)


if __name__ == '__main__':
    app.run(debug=True)
