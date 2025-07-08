from flask import Flask, jsonify
import random

app = Flask(__name__)

QUOTES = [
    "The best way to get started is to quit talking and begin doing.",
    "Don't let yesterday take up too much of today.",
    "It's not whether you get knocked down, it's whether you get up.",
    "If you are working on something exciting, it will keep you motivated."
]

@app.route('/quote')
def quote():
    return jsonify({'quote': random.choice(QUOTES)})

if __name__ == '__main__':
    app.run(debug=True) 