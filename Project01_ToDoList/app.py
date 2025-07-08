from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append({'task': task, 'done': False})
    return render_template('index.html', tasks=tasks)

@app.route('/complete/<int:task_id>')
def complete(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 