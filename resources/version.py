from flask_restful import Resource, reqparse
from models.version import VersionModel

class AppVersion(Resource):
    def get(self):
        version = VersionModel.find()
        if version:
            return version.json()
        return {'message': 'Item not found'}, 404
