import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files.get('file')
        if f:
            f.save(os.path.join(UPLOAD_FOLDER, f.filename))
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

if __name__ == '__main__':
    app.run(debug=True) 