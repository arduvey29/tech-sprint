from flask import Flask, render_template, request
import markdown

app = Flask(__name__)
posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            posts.append({'title': title, 'content': content})
    return render_template('index.html', posts=posts, markdown=markdown.markdown)

if __name__ == '__main__':
    app.run(debug=True) 