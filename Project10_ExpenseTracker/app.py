from flask import Flask, render_template, request

app = Flask(__name__)
expenses = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        desc = request.form.get('desc')
        amount = request.form.get('amount')
        if desc and amount:
            try:
                amount = float(amount)
                expenses.append({'desc': desc, 'amount': amount})
            except ValueError:
                pass
    total = sum(e['amount'] for e in expenses)
    return render_template('index.html', expenses=expenses, total=total)

if __name__ == '__main__':
    app.run(debug=True) 