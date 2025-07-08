from flask import Flask, render_template, request, redirect, url_for
import random, string

app = Flask(__name__)
urls = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        original = request.form.get('url')
        if original:
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            urls[code] = original
            short_url = request.host_url + code
    return render_template('index.html', short_url=short_url)

@app.route('/<code>')
def redirect_short(code):
    if code in urls:
        return redirect(urls[code])
    return 'Invalid URL', 404

if __name__ == '__main__':
    app.run(debug=True) 