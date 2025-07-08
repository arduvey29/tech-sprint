from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
votes = {'Option A': 0, 'Option B': 0}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        vote = request.form.get('vote')
        if vote in votes:
            votes[vote] += 1
    return render_template('index.html', votes=votes)

if __name__ == '__main__':
    app.run(debug=True) 