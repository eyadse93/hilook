from db import db
from sqlalchemy import or_
from sqlalchemy import and_

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

    @classmethod
    def filter(cls, user, results):
        usernames = []
        for result in results:
            usernames.append(result.username)
        blockedUsernames = cls.query.filter(or_(
            and_(
                BlockedUsersModel.userId.in_(usernames), BlockedUsersModel.blockedId==user.username
                ), and_(
                    BlockedUsersModel.blockedId.in_(usernames), BlockedUsersModel.userId==user.username
                )
            )
        ).all()
        print(len(blockedUsernames))
        for r in results:
            print("looping")
            for b in blockedUsernames:
                if r.username == b.userId or r.username == b.blockedId:
                    print("if")
                    results.remove(r)
        return results
