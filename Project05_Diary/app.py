from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
diary = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        entry = request.form.get('entry')
        if entry:
            diary.append(entry)
    return render_template('index.html', diary=diary)

@app.route('/delete/<int:entry_id>')
def delete(entry_id):
    if 0 <= entry_id < len(diary):
        diary.pop(entry_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 