import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel
from datetime import datetime

class UserLogin(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = UserLogin.parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user:
            if user.checkPassword(data['password']):
                return user.json(), 200
            else:
                return {"message": "wrong password"}, 400
        else:
            return {"message": "user not found"}, 400

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('name', type=str, required=False)
    parser.add_argument('gender', type=str, required=False)
    parser.add_argument('interested_in', type=str, required=False)
    parser.add_argument('latitude', type=float, required=False)
    parser.add_argument('longitude', type=float, required=False)
    parser.add_argument('image_url', type=str, required=False)
    parser.add_argument('hangout1', type=str, required=False)
    parser.add_argument('hangout2', type=str, required=False)
    parser.add_argument('hangout3', type=str, required=False)
    parser.add_argument('hangout4', type=str, required=False)
    parser.add_argument('active', type=bool, required=False)
    parser.add_argument('authentication_method', type=str, required=False)
    parser.add_argument('notification', type=bool, required=False)
    parser.add_argument('login', type=bool, required=False)
    parser.add_argument('hilook_visible', type=bool, required=False)
    parser.add_argument('hangouts_visible', type=bool, required=False)
    parser.add_argument('max_distance', type=float, required=False)
    parser.add_argument('hide_ads', type=bool, required=False)
    parser.add_argument('registration_ids', type=str, required=False)
    parser.add_argument('feet_or_meter', type=str, required=False)
    parser.add_argument('tips', type=str, required=False)
    parser.add_argument('email', type=str, required=False)
    parser.add_argument('birthdate', type=float, required=False)
    parser.add_argument('city', type=str, required=False)
    parser.add_argument('country', type=str, required=False)
    parser.add_argument('token', type=str, required=False)

    def post(self):
        data = UserRegister.parser.parse_args()
        print(data['username'])
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()
        return user.json(), 200


class GetUserData(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = GetUserData.parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user:
            return user.json(), 200
        else:
            return {"message": "user not found"}, 400

class SetUserData(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('name', type=str, required=False)
    parser.add_argument('gender', type=str, required=False)
    parser.add_argument('interested_in', type=str, required=False)
    parser.add_argument('latitude', type=float, required=False)
    parser.add_argument('longitude', type=float, required=False)
    parser.add_argument('image_url', type=str, required=False)
    parser.add_argument('hangout1', type=str, required=False)
    parser.add_argument('hangout2', type=str, required=False)
    parser.add_argument('hangout3', type=str, required=False)
    parser.add_argument('hangout4', type=str, required=False)
    parser.add_argument('active', type=bool, required=False)
    parser.add_argument('authentication_method', type=str, required=False)
    parser.add_argument('notification', type=bool, required=False)
    parser.add_argument('login', type=bool, required=False)
    parser.add_argument('hilook_visible', type=bool, required=False)
    parser.add_argument('hangouts_visible', type=bool, required=False)
    parser.add_argument('max_distance', type=float, required=False)
    parser.add_argument('hide_ads', type=bool, required=False)
    parser.add_argument('registration_ids', type=str, required=False)
    parser.add_argument('feet_or_meter', type=str, required=False)
    parser.add_argument('tips', type=str, required=False)
    parser.add_argument('email', type=str, required=False)
    parser.add_argument('birthdate', type=float, required=False)
    parser.add_argument('city', type=str, required=False)
    parser.add_argument('country', type=str, required=False)
    parser.add_argument('token', type=str, required=False)

    def post(self):
        data = SetUserData.parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user:
            for key, value in data.items():
                if (key == 'interested_in'):
                    user.interested_in = value
                else if (key == 'latitude'):
                    user.latitude = value
                else if (key == 'longitude'):
                    user.longitude = value
                else if (key == 'image_url'):
                    user.image_url = value
                else if (key == 'hangout1'):
                    user.hangout1 = value
                else if (key == 'hangout2'):
                    user.hangout2 = value
                else if (key == 'hangout3'):
                    user.hangout3 = value
                else if (key == 'hangout4'):
                    user.hangout4 = value
                else if (key == 'active'):
                    user.active = value
                else if (key == 'authentication_method'):
                    user.authentication_method = value
                else if (key == 'notification'):
                    user.notification = value
                else if (key == 'login'):
                    user.login = value
                else if (key == 'hilook_visible'):
                    user.hilook_visible = value
                else if (key == 'hangouts_visible'):
                    user.hangouts_visible = value
                else if (key == 'max_distance'):
                    user.max_distance = value
                else if (key == 'hide_ads'):
                    user.hide_ads = value
                else if (key == 'registration_ids'):
                    user.registration_ids = value
                else if (key == 'feet_or_meter'):
                    user.feet_or_meter = value
                else if (key == 'tips'):
                    user.tips = value
                else if (key == 'email'):
                    user.email = value
                else if (key == 'city'):
                    user.city = value
                else if (key == 'country'):
                    user.country = value
                else if (key == 'token'):
                    user.token = value
                    
            user.save_to_db()
            return user.json(), 200
        else:
            return {"message": "user not found"}, 400
