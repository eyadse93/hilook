from flask_restful import Resource, reqparse
from models.user import UserModel
from models.blockedUsers import BlockedUsersModel
from models.userData import UserDataModel

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

    parser.add_argument('skip',
        type=int
    )

    def post(self):
        skip = data['skip']
        pagination = 10 + skip
        data = GetHangouts.parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user:
            jsonResult = []
            results = UserModel.find_hangouts(user, data['filter'])
            #print(len(results))
            results = BlockedUsersModel.filter(user, results)
            #print(len(results))
            results = UserDataModel.filter(user, results)
            print("result num")
            print(len(results))
            flag = 0 + skip

            while flag < pagination:
                if len(results) > flag:
                    result = results[flag]
                    jsonResult.append(result.json())
                flag = flag + 1

            """
            for result in results:
                flag = flag + 1
                if (flag > pagination):
                    break
                else:
                    jsonResult.append(result.json())
            """
            return jsonResult
