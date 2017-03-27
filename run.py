from app import app
from db import db

import threading


db.init_app(app)


def f():
    # do something here ...
    # call f() again in 60 seconds
    print("eeezzz1234321")
    threading.Timer(10, f).start()

# start calling f now and every 60 sec thereafter
f()



@app.before_first_request
def create_tables():
    db.create_all()
