from db import db
from sqlalchemy import or_
from sqlalchemy import and_

class UserDataModel(db.Model):
    __tablename__ = 'userData'

    id = db.Column(db.Integer, primary_key=True)
    user1 = db.Column(db.String(80))
    user2 = db.Column(db.String(80))
    dataType = db.Column(db.String(80))
    looked = db.Column(db.Boolean)

    def __init__(self, userId, blockedId):
        self.userId = userId
        self.blockedId = blockedId

    def json(self):
        return {'user1': self.user1, 'user2': self.user2}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def filter(cls, user, results):
        usernames = []
        for result in results:
            usernames.append(result.username)
        userDataNames = cls.query.filter(or_(
            and_(
                UserDataModel.user1.in_(usernames), UserDataModel.user2==user.username
                ), and_(
                    UserDataModel.user2.in_(usernames), UserDataModel.user1==user.username
                )
            )
        ).all()
        print(len(userDataNames))
        for r in results:
            print("looping")
            for b in userDataNames:
                if r.username == b.user1 or r.username == b.user2:
                    print("if")
                    results.remove(r)
        return results
