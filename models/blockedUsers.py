from db import db

class BlockedUsersModel(db.Model):
    __tablename__ = 'blockedUsers'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.String(80))
    blockedId = db.Column(db.String(80))

    def __init__(self, userId, blockedId):
        self.userId = userId
        self.blockedId = blockedId

    def json(self):
        return {'userId': self.userId, 'blockedId': self.blockedId}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
