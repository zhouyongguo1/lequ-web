from datetime import datetime
from enum import unique, Enum

from lequ import db
from lequ.sqltype import Enum as sqlEnum

@unique
class ProjectStatus(Enum):
    start = 1
    finish = 2
    stop = 3


@unique
class TaskStatus(Enum):
    none = None
    start = 1
    finish = 2
    stop = 3


class Project(db.Model):
    __tablename__ = 'pro_project'

    id = db.Column(db.Integer, primary_key=True)
    teamId = db.Column('team_id', db.Integer)
    name = db.Column(db.String)
    status = db.Column(sqlEnum(ProjectStatus), default=ProjectStatus.start)
    isArchived = db.Column('is_archived', db.Boolean, default=False)
    isDel = db.Column('is_del', db.Boolean, default=False)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.BigInteger)

    def __init__(self, teamId, name):
        self.name = name
        self.teamId = teamId
        self.created_by = 1
        self.created_at = datetime.now()
        self.updated_by = 1
        self.updated_at = datetime.now()

#
# class Task(db.Model):
#     __tablename__ = 'pro_task'
#
#     id = db.Column(db.Integer, primary_key=True)
#     teamId = db.Column('team_id', db.Integer)
#     name = db.Column(db.String)
#     projetId = db.Column('project_id', db.Integer, db.ForeignKey('Project.id'))
#     project = db.relationship('Project')
#     content = db.Column(db.text)
#     points = db.Column(db.Integer, default=0)
#     pri = db.Column(db.Integer, default=0)
#     isArchived = db.Column('is_archived', db.Boolean, default=False)
#     isDel = db.Column('is_del', db.Boolean, default=False)
#     sequence = db.Column(db.Integer, default=0)
#     status = db.Column(myEnum(TaskStatus), default=TaskStatus.none)
#     planEndDate = db.Column('plan_end_date', db.DateTime)
#     endDate = db.Column('end_date', db.DateTime)
#
#     ownerId = db.Column('owner_id', db.Integer, db.ForeignKey('User.id'))
#     owner = db.relationship("User", backref="Task")
#
#     def __init__(self, teamId, name, project, content):
#         self.name = name
#         self.teamId = teamId
#         self.project = project
#         self.content = content
