import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister, UserLogin, GetUserData, SetUserData, UserDelete
from resources.hangouts import GetHangouts
from resources.version import AppVersion

import threading

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(AppVersion, '/version')
api.add_resource(UserLogin, '/login')
api.add_resource(UserRegister, '/register')
api.add_resource(GetUserData, '/getuserdata')
api.add_resource(SetUserData, '/setuserdata')
api.add_resource(UserDelete, '/deleteuser')
api.add_resource(GetHangouts, '/gethangouts')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
