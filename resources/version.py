from flask_restful import Resource, reqparse
from models.version import VersionModel

class AppVersion(Resource):
    def get(self):
        #return {'message': 'this is the app version'}

        if VersionModel.hasRecord() == False:
            version = VersionModel(1.9, 1.9)
            version.save_to_db()

        version = VersionModel.find()
        if version:
            return version.json()
        return {'message': 'Item not found'}, 404
