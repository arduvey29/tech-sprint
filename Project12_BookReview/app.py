from flask import Flask, render_template, request

app = Flask(__name__)
books = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        review = request.form.get('review')
        rating = request.form.get('rating')
        if title and review and rating:
            books.append({'title': title, 'review': review, 'rating': rating})
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True) 