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


@app.route('/orders_in_progress')
def orders_in_progress():
    _msg = "See things that have been ordered here"
    return render_template('review_orders.html', msg=_msg)


@app.route('/orders_complete')
def orders_complete():
    _msg = "See completed orders here"
    return render_template('update_order.html', msg=_msg)

@app.route('/balance')
def balance():
    user = request.args['user']
    _balance = "The balance of " + user + " is 1999"
    return render_template('balance.html', balance=_balance)

@app.route('/profile')
def profile():
    user_id = request.args['user_id']
    _msg = "The profile for " + user_id
    return render_template('profile.html', msg=_msg)

if __name__ == '__main__':
    app.run(debug=True, port=1000)