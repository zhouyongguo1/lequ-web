from flask import g
from wtforms import Form, StringField
from wtforms.validators import DataRequired

from lequ.project.models import Project


class ProjectForm(Form):
    name = StringField(validators=[DataRequired()])

    def to_project(self):
        pro = Project(g.team_id, self.name.data)
        return pro
