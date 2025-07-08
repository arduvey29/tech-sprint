from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@socketio.on('send_message')
def handle_send_message(data):
    messages.append(data['message'])
    emit('receive_message', data['message'], broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True) 