from flask import Flask, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)


@app.route('/update')
def update():
    status = jsonify(request.args['status'])
    socketio.emit("status", broadcast=True)
    return "updating provider status " + str(status)


@app.route('/start')
def start():
    return "starting order"


@app.route('/complete')
def complete():
    return "completing order"


@app.route('/acknowledge')
def acknowledge():
    return "acknowledging order"


if __name__ == '__main__':
    socketio.run(app, port=2000)
