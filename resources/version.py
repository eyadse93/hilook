from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.version import VersionModel
class AppVersion(Resource):

    @jwt_required()
    def get(self):

        if VersionModel.hasRecord == False:
            version = VersionModel(1.9, 1.9)
            version.save_to_db()

        version = VersionModel.find_by_name(name)
        if version:
            return version.json()
        return {'message': 'Item not found'}, 404
