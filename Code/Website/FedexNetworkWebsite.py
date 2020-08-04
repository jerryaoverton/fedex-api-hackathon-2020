from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', content='Start by registering a user')


@app.route('/register')
def register():
    _user = request.args['user']
    return render_template('register.html', user=_user)


@app.route('/shop')
def shop():
    _items = ['coffee', 'tea', 'milk', 'eggs', 'bread']
    return render_template('shop.html', items=_items)


@app.route('/pay')
def pay():
    _msg = "This is where you pay $$$"
    return render_template('pay.html', msg=_msg)


@app.route('/orders_in_progress')
def orders_in_progress():
    _msg = "See things that have been ordered here"
    return render_template('orders_in_progress.html', msg=_msg)


@app.route('/orders_complete')
def orders_complete():
    _msg = "See completed orders here"
    return render_template('orders_complete.html', msg=_msg)

@app.route('/balance')
def balance():
    user = request.args['user']
    _balance = "The balance of " + user + " is 1999"
    return render_template('balance.html', balance=_balance)

@app.route('/profile')
def profile():
    user = request.args['user']
    _msg = "The profile for " + user
    return render_template('profile.html', msg=_msg)

if __name__ == '__main__':
    app.run(debug=True, port=1000)