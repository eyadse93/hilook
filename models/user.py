import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    name = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    interested_in = db.Column(db.String(80))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    image_url = db.Column(db.String(80))
    hangout1 = db.Column(db.String(80))
    hangout2 = db.Column(db.String(80))
    hangout3 = db.Column(db.String(80))
    hangout4 = db.Column(db.String(80))
    active = db.Column(db.Bool)
    authentication_method = db.Column(db.String(80))
    notification = db.Column(db.Bool)
    login = db.Column(db.Bool)
    hilook_visible = db.Column(db.Bool)
    hangouts_visible = db.Column(db.Bool)
    max_distance = db.Column(db.Int)
    hide_ads = db.Column(db.Bool)
    registration_ids = db.Column(db.JSON)
    feet_or_meter = db.Column(db.Bool)
    tips = db.Column(db.ARRAY(String))
    email = db.Column(db.String(80))
    birthdate = db.Column(db.String(80))
    city = db.Column(db.String(80))
    country = db.Column(db.String(80))
    token = db.Column(db.String(80))



    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {'username': self.username}

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
