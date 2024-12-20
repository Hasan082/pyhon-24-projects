from flask import Flask, request
from random import randint, choice
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    phrase: list[str] = ['Welcome to this page!', 'You are looking good today!', 'The weather is great!']
    return {
        'phrase': choice(phrase),
        'data': datetime.now()
    }


@app.route('/random')
def random():
    number_input = request.args.get('number', default=100, type=int)
    text_input = request.args.get('text', default="Default Text", type=str)

    if isinstance(number_input, int):
        return {
            'input': number_input,
            'text': text_input,
            'random': randint(1, number_input),
            'date': datetime.now()
        }
    else:
        return {
            'Error': "Please enter an integer.",
            'text': text_input,
            'date': datetime.now()
        }


if __name__ == '__main__':
    app.run(debug=True)
