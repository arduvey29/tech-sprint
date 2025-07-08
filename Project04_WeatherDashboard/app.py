from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form.get('city')
        # Mock response
        weather = f"Weather in {city}: Sunny, 25°C"
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True) 