import requests
from flask import Flask, render_template, request
app = Flask(__name__)

fedex_token_network = 'http://127.0.0.1:5000/'


@app.route('/')
def home():
    return render_template('index.html', content='Start by registering a user')


@app.route('/register')
def register():
    user_id = request.args['user_id']

    # register user with the smart contract
    svc = '/register_user'
    params = '?user_id=' + user_id
    url = fedex_token_network + svc + params
    _msg = requests.get(url).content

    return render_template('register.html', msg=_msg)


@app.route('/shop')
def shop():
    _content = "Here is some stuff you can buy"
    return render_template('shop.html', content=_content)


@app.route('/pay')
def pay():
    _msg = "This is where you pay $$$"
    return render_template('pay.html', msg=_msg)


@app.route('/update_order')
def update_order():
    _msg = "create or update your order here"
    return render_template('update_order.html', msg=_msg)


@app.route('/review_orders')
def review_orders():
    _msg = "See updated orders here"
    return render_template('review_orders.html', msg=_msg)


@app.route('/balance')
def balance():
    user_id = request.args['user_id']

    # get the user's balance from the smart contract
    svc = '/user_balance'
    params = '?user_id=' + user_id
    url = fedex_token_network + svc + params
    _balance = requests.get(url).content

    _msg = "The balance of " + user_id + " is " + str(_balance)
    return render_template('balance.html', msg=_msg)


@app.route('/profile')
def profile():
    user_id = request.args['user_id']
    _msg = "The profile for " + user_id
    return render_template('profile.html', msg=_msg)

if __name__ == '__main__':
    app.run(debug=True, port=1000)