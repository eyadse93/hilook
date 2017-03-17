from flask_restful import Resource, reqparse

class AppVersion(Resource):
    def get(self):
        return {'message': 'this is the app version'}
