from flask_restful import Resource, reqparse
from models.user import UserModel
from models.blockedUsers import BlockedUsersModel

from db import db

class GetHangouts(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    parser.add_argument('filter',
        type=int,
        help="0: all, 1: 18-25, 2: 26-33, 3: 34-41, 4: 42-50, 5: above 50"
    )

    def post(self):
        data = GetHangouts.parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user:
            jsonResult = []
            results = UserModel.find_hangouts(user, data['filter'])

            results = BlockedUsersModel.filter(user, results)

            for result in results:
                jsonResult.append(result.json())
            return jsonResult
            #print (result)
