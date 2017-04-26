import sqlite3
from db import db
from datetime import datetime
from sqlalchemy import or_
from sqlalchemy import and_
import time

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    name = db.Column(db.String)
    gender = db.Column(db.String)
    interested_in = db.Column(db.String)
    latitude = db.Column(db.BigInteger)
    longitude = db.Column(db.BigInteger)
    image_url = db.Column(db.String)
    hangout1 = db.Column(db.String)
    hangout2 = db.Column(db.String)
    hangout3 = db.Column(db.String)
    hangout4 = db.Column(db.String)
    active = db.Column(db.Boolean)
    authentication_method = db.Column(db.String)
    notification = db.Column(db.Boolean)
    login = db.Column(db.Boolean)
    hilook_visible = db.Column(db.Boolean)
    hangouts_visible = db.Column(db.Boolean)
    max_distance = db.Column(db.BigInteger)
    hide_ads = db.Column(db.Boolean)
    registration_ids = db.Column(db.String)
    feet_or_meter = db.Column(db.String)
    tips = db.Column(db.String)
    email = db.Column(db.String)
    birthdate = db.Column(db.BigInteger)
    city = db.Column(db.String)
    country = db.Column(db.String)
    token = db.Column(db.String)

    def __init__(self, username, password
    , name, gender, interested_in, latitude
    , longitude, image_url
    , hangout1, hangout2, hangout3, hangout4, active,
    authentication_method, notification, login, hilook_visible, hangouts_visible,
    max_distance, hide_ads, registration_ids, feet_or_meter, tips, email
    ,birthdate, city, country, token
    ):
        self.username = username
        self.password = password
        self.name = name
        self.gender = gender
        self.interested_in = interested_in
        self.latitude = latitude
        self.longitude = longitude
        self.image_url = image_url
        self.hangout1 = hangout1
        self.hangout2 = hangout2
        self.hangout3 = hangout3
        self.hangout4 = hangout4
        self.active = active
        self.authentication_method = authentication_method
        self.notification = notification
        self.login = login
        self.hilook_visible = hilook_visible
        self.hangouts_visible = hangouts_visible
        self.max_distance = max_distance
        self.hide_ads = hide_ads
        self.registration_ids = registration_ids
        self.feet_or_meter = feet_or_meter
        self.tips = tips
        self.email = email
        self.birthdate = birthdate
        self.city = city
        self.country = country
        self.token = token

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {'username': self.username, 'password': self.password
        , 'name':self.name,
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
        'email': self.email
        ,'birthdate': self.birthdate,
        'city': self.city, 'country': self.country,
        'token': self.token
        }

    def checkPassword(self, password):
        if self.password == password:
            return True
        return False

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_hangouts(cls, user, f):
        oneYearTime = 31556952000.0
        timeNow = time.time() * 1000.0
        minAge = timeNow
        maxAge = 0.0

        gender = "male"
        if user.interested_in == "men":
            gender = "male"
        else:
            gender = "female"

        interested_in = "men"
        if user.gender == "male":
            interested_in = "men"
        else:
            interested_in = "women"


        if f==1:
            minAge = timeNow - (18.0 * oneYearTime)
            maxAge = timeNow - (25.0 * oneYearTime)
            print("timeNow:" + str(timeNow))
            print("minAge:" + str(minAge))
            print("maxAge:" + str(maxAge))
            #max:  704237795961
            #user: 735779017393
            #min:  925136459961
        elif f==2:
            minAge = timeNow - (26.0 * oneYearTime)
            maxAge = timeNow - (33.0 * oneYearTime)
        elif f==3:
            minAge = timeNow - (34.0 * oneYearTime)
            maxAge = timeNow - (41.0 * oneYearTime)
        elif f==4:
            minAge = timeNow - (42.0 * oneYearTime)
            maxAge = timeNow - (50.0 * oneYearTime)
        elif f==5:
            minAge = timeNow - (50.0 * oneYearTime)
            maxAge = timeNow - (100.0 * oneYearTime)
            #sort by distance http://stackoverflow.com/questions/29013805/how-to-order-a-geospatial-query-by-distance-from-the-query-point
        result = (
            cls.query.filter(or_(
                UserModel.hangout1==user.hangout1,
                 UserModel.hangout2==user.hangout2,
                  UserModel.hangout3==user.hangout3,
                   UserModel.hangout4==user.hangout4,
                    UserModel.city==user.city
            ), UserModel.country==user.country, UserModel.username != user.username, and_(
                UserModel.birthdate >= maxAge, UserModel.birthdate <= minAge
            ), UserModel.gender==gender, UserModel.interested_in==interested_in, UserModel.active, UserModel.hangouts_visible, or_(
                and_(BlockedUsers.user_id==user.username, BlockedUsers.blocked_id==UserModel.username),and_(
                    BlockedUsers.user_id==UserModel.username, BlockedUsers.blocked_id==user.username))).limit(20).all()
        )
        return result
