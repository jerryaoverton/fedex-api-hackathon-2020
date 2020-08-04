from flask import Flask, request, jsonify
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')
def handle_message(msg):
    print('Message ' + msg)
    send(msg, broadcast=True)


@app.route('/start')
def start():
    return "starting order"


@app.route('/complete')
def complete():
    return "completing order"


@app.route('/acknowledge')
def acknowledge():
    return "acknowledging order"


@app.route('/update')
def update():
    service = request.args['service']
    status = request.args['status']
    msg = str(service) + " is now " + str(status)
    socketio.send(msg, broadcast=True)
    return "updating provider status " + str(status)


if __name__ == '__main__':
    socketio.run(app, debug=True)