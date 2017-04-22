from flask_restful import Resource, reqparse
from models.user import UserModel

class GetHangouts(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = GetHangouts.parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user:
            result = UserModel.find_hangouts(user.username, user.hangout1, user.hangout2, user.hangout3, user.hangout4, user.country)
            print (result)
