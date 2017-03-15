from db import db

class VersionModel(db.Model):
    __tablename__ = 'version'

    id = db.Column(db.Integer, primary_key=True)
    android_version = db.Column(db.Float)
    ios_version = db.Column(db.Float)

    def __init__(self, android_version, ios_version):
        self.android_version = android_version
        self.ios_version = ios_version

    def json(self):
        return {'android_version': self.android_version, 'ios_version': self.ios_version}

    @classmethod
    def find(cls):
        return cls.query.first()

    @classmethod
    def hasRecord(cls):
        if cls.query.first():
            return True
        return False

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
