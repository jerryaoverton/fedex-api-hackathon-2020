from flask import Flask, request, jsonify
from flask_socketio import SocketIO, send
import ast

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, cors_allowed_origins="*")

order_example = {'supplier': '123abc',
                 'customer': '456xyz',
                 'payment_method': 'tokens',
                 'price': 100,
                 'order_details': 'charge the drone to 100%',
                 'terms_and_conditions': 'must not harm drone',
                 'status': 'complete',
                 'status_date': '08/05/2020'
                 }

profile_example = {'image_url': 'www.pic.com/profile.jpg',
                   'profile_url': 'www.myprofile.com',
                   'description': 'A great and powerful technologist',
                   'tags': 'drone_tech, programmer',
                   'rating': 3,
                   'status': 'active'
                   }

user_example = {'id': "123xyz", 'tokens': 0, 'profile': profile_example}

users = []

# TODO: remove this
@socketio.on('message')
def handle_message(msg):
    print('Message ' + msg)
    send(msg, broadcast=True)


@app.route('/register_user')
def register_user():
    user_id = request.args['user_id']
    user = {'id': user_id, 'tokens': 0, 'profile': ''}
    users.append(user)

    return user_id + ' is registered'


@app.route('/update_profile')
def update_profile():
    print('entered the update profile')
    user_id = request.args['user_id']
    profile_string = request.args['profile']

    profile_dict = ast.literal_eval(profile_string)

    for user in users:
        if user['id'] == user_id:
            user['profile'] = profile_dict
            print('updating profile')
            socketio.send(str(user), namespace='/profile', broadcast=True)

    return "profile updated"


@app.route('/user_profile')
def user_profile():
    user_id = request.args['user_id']

    profile = ""
    for user in users:
        if user['id'] == user_id:
            profile = user['profile']

    return profile


@app.route('/user_balance')
def user_balance():
    user_id = request.args['user_id']

    balance = 0
    for user in users:
        if user['id'] == user_id:
            balance = user['tokens']

    return str(balance)


@app.route('/update_order')
def update_order():
    order = request.args['order']
    socketio.send(str(order), namespace='/order', broadcast=True)

    return "order updated"


@app.route('/pay')
def pay():
    sender = request.args['sender']
    receiver = request.args['receiver']
    amt = int(request.args['amount'])

    for user in users:
        if user['id'] == sender:
            user['tokens'] -= amt
        if user['id'] == receiver:
            user['tokens'] += amt

    return "paid"

if __name__ == '__main__':
    socketio.run(app, debug=True)
