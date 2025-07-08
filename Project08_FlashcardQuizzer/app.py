from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
flashcards = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form.get('question')
        answer = request.form.get('answer')
        if question and answer:
            flashcards.append({'question': question, 'answer': answer})
    return render_template('index.html', flashcards=flashcards)

@app.route('/quiz/<int:card_id>')
def quiz(card_id):
    if 0 <= card_id < len(flashcards):
        card = flashcards[card_id]
        return render_template('quiz.html', card=card)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 