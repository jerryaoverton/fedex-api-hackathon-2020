from time import sleep
import socketio
import requests

ctx = {'current_job': '',
       'max_total_jobs': 10,
       'max_consecutive_jobs': 3,
       'total_jobs': 0,
       'jobs_since_maintenance': 0}

sio = socketio.Client()
sio.connect('http://localhost:5000', namespaces=['/profile', '/order'])

profile = {'image_url': 'www.pic.com/drone.jpg',
           'profile_url': 'www.mydroneprofile.com',
           'description': 'A very useful drone',
           'tags': 'drone, delivery',
           'rating': 5,
           'status': 'idle'
           }
fedex_token_network = 'http://127.0.0.1:5000/'


def register_drone():
    svc = '/register_user'
    params = '?user_id=drone'
    url = fedex_token_network + svc + params
    _msg = requests.get(url).content


def update_profile():
    svc = '/update_profile'
    params = '?user_id=drone&profile=' + str(profile)
    url = fedex_token_network + svc + params
    _msg = requests.get(url).content


def update_order(order):
    svc = '/update_order'
    params = '?order=' + str(order)
    url = fedex_token_network + svc + params
    _msg = requests.get(url).content


@sio.on('message', namespace='/order')
def on_message(order):
    # choose a job
    # TODO: pick a job based on it's status
    if "drone" in order:
        ctx['current_job'] = order


def wait():
    profile['status'] = 'waiting'
    update_profile()
    sleep(10)

    end_of_life = ctx['total_jobs'] >= ctx['max_total_jobs']
    hired = not (ctx['current_job'] == '')

    if end_of_life:
        retire()
    elif hired:
        work()
    else:
        wait()


def work():
    ctx['jobs_since_maintenance'] += 1
    ctx['total_jobs'] += 1

    profile['status'] = 'working'
    update_profile()

    sleep(10)
    # TODO: update the order status
    ctx['current_job'] = ''

    jobs_since_maintenance = ctx['jobs_since_maintenance']
    max_consecutive_jobs = ctx['max_consecutive_jobs']
    if jobs_since_maintenance < max_consecutive_jobs:
        wait()
    else:
        get_maintenance()


def get_maintenance():
    profile['status'] = 'under maintenance'
    update_profile()

    ctx['jobs_since_maintenance'] = 0
    sleep(10)
    pay_for_maintenance()


def pay_for_maintenance():
    profile['status'] = 'paying for maintenance'
    update_profile()
    sleep(10)
    wait()


def retire():
    profile['status'] = 'retired'
    update_profile()
    print("drone is retired")


register_drone()
wait()

