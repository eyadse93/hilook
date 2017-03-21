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
    active = db.Column(db.Boolean)
    authentication_method = db.Column(db.String(80))
    notification = db.Column(db.Boolean)
    login = db.Column(db.Boolean)
    hilook_visible = db.Column(db.Boolean)
    hangouts_visible = db.Column(db.Boolean)
    max_distance = db.Column(db.Integer)
    hide_ads = db.Column(db.Boolean)
    registration_ids = db.Column(db.JSON)
    feet_or_meter = db.Column(db.Boolean)
    tips = db.Column(db.JSON)
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
        return {'username': self.username, 'name': self.name,
        'gender': self.gender, 'interested_in': self.interested_in,
        'latitude': self.latitude, 'longitude': self.longitude,
        'image_url': self.image_url, 'hangout1': self.hangout1,
        'hangout2': self.hangout2, 'hangout3': self.hangout3,
        'hangout4': self.hangout4, 'active': self.active,
        'authentication_method': self.authentication_method, 'notification': self.notification,
        'login': self.login, 'hilook_visible': self.hilook_visible,
        'hangouts_visible': self.hangouts_visible, 'max_distance': self.max_distance,
        'hide_ads': self.hide_ads, 'registration_ids': self.registration_ids,
        'feet_or_meter': self.feet_or_meter, 'tips': self.tips,
        'email': self.email, 'birthdate': self.birthdate,
        'city': self.city, 'country': self.country,
        'token': self.token}

    def checkPassword(self, password):
        if self.password == password:
            return true
        return false

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
