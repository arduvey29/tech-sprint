from flask import Flask, render_template, request

app = Flask(__name__)
recipes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        desc = request.form.get('desc')
        if name and desc:
            recipes.append({'name': name, 'desc': desc})
    return render_template('index.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True) 