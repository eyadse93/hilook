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
            #results = UserModel.find_hangouts(user)
            results = GetHangouts.find_hangouts(user)
            for result in results:
                #jsonResult = jsonResult + result.json()
                jsonResult.append(result.json())
            return jsonResult
            #print (result)

    @classmethod
    def find_hangouts(cls, user):
        #we can move this to hangouts class
        result = (
            cls.query.filter(or_(
                UserModel.hangout1==user.hangout1,
                 UserModel.hangout2==user.hangout2,
                  UserModel.hangout3==user.hangout3,
                   UserModel.hangout4==user.hangout4,
                    UserModel.city==user.city
            ), UserModel.country==user.country, UserModel.username != user.username).limit(20).all()
        )
        return result
