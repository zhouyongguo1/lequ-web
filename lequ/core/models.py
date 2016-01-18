from datetime import datetime

from lequ import db


class Team(db.Model):
    __tablename__ = 'core_team'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)

    def __init__(self, name, created_by):
        self.name = name
        self.created_by = created_by
        self.created_at = datetime.now()


class User(db.Model):
    __tablename__ = 'core_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    passWorld = db.Column('pass', db.String)
    email = db.Column(db.String)
    wechat = db.Column(db.String)
    phone = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.BigInteger)

    def __init__(self):
        self.name = 'name'
        self.passWorld = 'pass'
        self.email = 'email'
        self.wechat = 'wechat'
        self.phone = 'phone'
        self.created_at = datetime.now()
        self.created_by = 1
        self.updated_at = datetime.now()
        self.updated_by = 1



