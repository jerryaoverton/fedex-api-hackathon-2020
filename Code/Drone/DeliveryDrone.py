from time import sleep
import socketio

ctx = {'data': '',
       'max_total_jobs': 10,
       'max_consecutive_jobs': 3,
       'total_jobs': 0,
       'jobs_since_maintenance': 0}

sio = socketio.Client()
sio.connect('http://localhost:5000')


@sio.on('message')
def on_message(msg):
    ctx['data'] = msg


def wait():
    print("drone is idle")
    sleep(5)
    end_of_life = ctx['total_jobs'] >= ctx['max_total_jobs']
    hired = "drone" in ctx['data']
    if end_of_life:
        retire()
    elif hired:
        work()
    else:
        wait()


def retire():
    print("drone has retired")


def work():
    ctx['jobs_since_maintenance'] += 1
    ctx['total_jobs'] += 1
    print("drone is working")
    sleep(5)
    ctx['data'] = ''

    jobs_since_maintenance = ctx['jobs_since_maintenance']
    max_consecutive_jobs = ctx['max_consecutive_jobs']
    if jobs_since_maintenance < max_consecutive_jobs:
        wait()
    else:
        get_maintenance()


def get_maintenance():
    print("drone is getting maintenance")
    ctx['jobs_since_maintenance'] = 0
    sleep(5)
    pay_for_maintenance()


def pay_for_maintenance():
    print("drone is paying for maintenance")
    sleep(5)
    wait()


def retire():
    print("drone is retired")


wait()

