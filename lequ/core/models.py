from datetime import datetime

from flask.ext.login import UserMixin

from lequ import db


class User(UserMixin, db.Model):
    __tablename__ = 'core_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    password = db.Column('pass', db.String)
    email = db.Column(db.String)
    wechat = db.Column(db.String)
    phone = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.BigInteger)

    def __init__(self, name, password, email, wechat, phone, owner_id):
        self.name = name
        self.password = password
        self.email = email
        self.wechat = wechat
        self.phone = phone
        self.created_at = datetime.now()
        self.created_by = owner_id
        self.updated_at = datetime.now()
        self.updated_by = owner_id

    # def password(self, password):
    #     self.password = generate_password_hash(password)

    def verify_password(self, password):
        return True
        # return self.password == password

        # return check_password_hash(self.password, password)


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


class Role(db.Model):
    __tablename__ = 'core_role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    team_id = db.Column(db.Integer)
    status = db.Column(db.Integer)

    def __init__(self, name, team_id):
        self.name = name
        self.team_id = team_id
        self.status = 1


class UserTeam(db.Model):
    __tablename__ = 'core_user_team'

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('core_team.id'))
    team = db.relationship('Team')
    user_id = db.Column(db.Integer, db.ForeignKey('core_user.id'))
    user = db.relationship('User')
    role_id = db.Column(db.Integer, db.ForeignKey('core_role.id'))
    role = db.relationship('Role')

    is_owner = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)

    def __init__(self, team, user, role=None, is_owner=False, created_by=None):
        self.team = team
        self.user = user
        self.role = role
        self.is_owner = is_owner
        self.created_by = created_by
        self.created_at = datetime.now()
