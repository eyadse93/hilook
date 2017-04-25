from flask_restful import Resource, reqparse
from models.user import UserModel
from db import db

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
            jsonResult = []
            results = UserModel.find_hangouts(user)
            for result in results:
                jsonResult.append(result.json())
            return jsonResult
            #print (result)
